from pathlib import Path
from typing import Dict

from turbo_docs.constants import CODE_EXTENSIONS
from turbo_docs.llm import count_tokens, get_completion_stream


def get_files(max_lines: int = 1000) -> Dict[Path, str]:
    """
    Recursively list all files in the current directory

    - Skip files that contain folders starting with .
    - Skip files that have a suffix that is not in CODE_EXTENSIONS
    - Skip files that are not files (e.g. directories)
    - Skip files that are named README.md (this will contaminate our generation)
    - Skip files that have more than max_lines lines

    :param max_lines: Maximum number of lines allowed in a file
    :return: Dictionary of Path to file content
    """
    files = {}
    for file in Path(".").glob("**/*"):
        if any(part.startswith(".") for part in file.parts):
            continue
        if file.suffix not in CODE_EXTENSIONS:
            continue
        if not file.is_file():
            continue
        if file.name.lower() == "readme.md":
            continue

        with open(file, "rb") as f:
            if f.read().count(b"\n") > max_lines:
                continue

        files[file] = file.read_text()

    return files


def files_to_str(files: Dict[Path, str]) -> str:
    """
    Convert a dictionary of files to a string
    """
    filestr = ""
    for file, content in files.items():
        filestr += f"# {file.name}\n\n"
        filestr += content
        filestr += "\n\n"
    return filestr


async def generate_readme(repo_str: str) -> str:
    """
    Generate a README.md file from the repository string.
    """
    readme = ""
    generator = await get_completion_stream(
        message=f"Generate a README.md file in markdown format (no triple backticks needed) from the following repository:\n\n\n{repo_str}"
    )
    async for chunk in generator:
        print(chunk, end="", flush=True)
        readme += chunk
    return readme


async def generate() -> None:
    """
    Recursively list all files in the current directory skipping paths that contain folders starting with .
    Returns absolute paths for all files.
    """

    files = get_files()
    repo_str = files_to_str(files)
    num_tokens = count_tokens(repo_str)

    print(f"Generating README.md (ingesting {num_tokens} tokens)")
    readme = await generate_readme(repo_str)

    print("Saving README.md")
    with open("README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    generate()
