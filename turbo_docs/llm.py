import json
import os
from typing import AsyncGenerator, Dict, List, Optional, Type, Union

import tiktoken
from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAIError
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from pydantic import BaseModel, ValidationError

load_dotenv()


class OpenAIClientError(Exception):
    """
    Exception raised when the OpenAI client fails to initialize.
    """


def get_client() -> AsyncOpenAI:
    try:
        return AsyncOpenAI()
    except OpenAIError as e:
        if "OPENAI_API_KEY" not in os.environ:
            raise OpenAIClientError("Looks like you are missing the OPENAI_API_KEY environment variable.")
        raise OpenAIClientError(f"Failed to initialize OpenAI client: {e}")


client = get_client()


def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """
    Returns the number of tokens in the provided text for the GPT-4o model.

    :param text: The input text to tokenize.
    :return: The number of tokens.
    """
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


async def _get_completion(
    messages: List[ChatCompletionMessage],
    model: str = "gpt-4o",
    response_format: Optional[Dict] = None,
    stream: bool = False,
) -> Union[str, AsyncGenerator[str, None]]:
    """
    Internal completion function that handles both streaming and non-streaming responses
    """
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        response_format=response_format,
        stream=stream,
    )

    if not stream:
        return response.choices[0].message.content

    async def content_generator():
        async for chunk in response:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    return content_generator()


async def get_completion(
    message: str,
    model: Optional[str] = "gpt-4o",
):
    """
    LLM completion with raw string response

    :param message: The message to send to the LLM.
    :param model: The model to use for the completion.
    :return: The raw string response from the LLM.
    """
    messages = [{"role": "user", "content": message}]
    return await _get_completion(messages=messages, model=model)


async def get_completion_stream(
    message: str,
    model: str = "gpt-4o",
) -> AsyncGenerator[str, None]:
    """
    Streams LLM completion responses as they're generated

    :param message: The message to send to the LLM
    :param model: The model to use for completion
    :return: Async generator yielding response chunks as strings
    """
    messages = [{"role": "user", "content": message}]
    return await _get_completion(messages=messages, model=model, stream=True)


async def get_completion_json(
    message: str,
    response_model: Type[BaseModel],
    model: str = "gpt-4o",
    max_retries: int = 3,
) -> BaseModel:
    """
    Get a JSON completion from the LLM and parse it into a Pydantic model.

    :param message: The message to send to the LLM.
    :param response_model: The Pydantic model to parse the response into.
    :param model: The model to use for the completion.
    :param max_retries: The maximum number of retries to attempt.
    :return: parsed Pydantic model
    """
    response_model_content = f"Your json response must follow the following: {response_model.schema()=}"

    messages = [
        {
            "role": "system",
            "content": f"You are a helpful assistant designed to output JSON. Do not use newline characters or spaces for json formatting. {response_model_content}",
        },
        {"role": "user", "content": message},
    ]

    response_str = "Completion failed."
    for attempt in range(max_retries):
        try:
            response_str = await _get_completion(
                model=model,
                messages=messages,
                response_format={"type": "json_object"},
            )
            response = json.loads(response_str)
            return response_model(**response)
        except (json.JSONDecodeError, ValidationError) as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to parse JSON after {max_retries} attempts: {e}")
        except Exception as e:
            raise Exception(f"Failed to get a valid response: {response_str=}, {e=}")

    raise Exception(f"Failed to get a valid response after {max_retries} attempts")
