# Turbo-Docs

Turbo-Docs is a versatile tool designed to simplify documentation generation for your Python projects. It leverages OpenAI's GPT models to create insightful and comprehensive README files directly from the repository structure and source code.

## Features

- **Automatic README Generation:** Turbo-Docs auto-generates README files using repository content and metadata.
- **Flexible Token Counting:** Uses `tiktoken` to handle tokenization, compatible with various model sizes and types.
- **PDM Build System Compatibility:** Integrates with PDM for Python dependency management.
- **Runs with Python 3.11 or higher:** Ensures compatibility with latest Python features and security upgrades.

## Installation

Install Turbo-Docs using your package manager with the following dependencies:

```shell
pip install tiktoken openai pydantic python-dotenv
```

Ensure your environment is using Python 3.11 or higher.

## Usage

Turbo-Docs provides a command-line interface (CLI) to generate documentation effortlessly.

### Command-Line Interface

Generate a README by executing:

```shell
turbo-docs --readme
```

## Configuration

### Environment Variables

Turbo-Docs requires `OPENAI_API_KEY` to be set in your environment to access OpenAI services.

```shell
export OPENAI_API_KEY="your-openai-api-key"
```

### Dependencies

Ensure the following dependencies are set in your `pyproject.toml` file:

- `tiktoken>=0.9.0`
- `openai>=1.63.2`
- `pydantic>=2.10.6`
- `python-dotenv>=1.0.1`

## Development

### Setting Up

To set up the development environment, make sure to configure PDM for managing project dependencies:

```shell
pdm install
```

### Running Locally

Run the CLI or other scripts using:

```shell
python -m turbo_docs.cli
```

## Project Structure

- **turbo_docs/**: Main package directory containing modules and scripts.
- **cli.py**: CLI entry point for the turbo-docs tool.
- **llm.py**: Functions for interaction with language models.
- **constants.py**: Holds configuration constants related to file extensions and directories.
- **readme.py**: Script for gathering files and generating README content.
- **pyproject.toml**: Project configuration file for dependencies, scripts, and PDM settings.

## Contributing

Please see our contributing guide for details on submitting patches and pull requests.

## License

This project is licensed under the MIT License.

## Authors

Created by Voynow (voynow99@gmail.com)

## Acknowledgments

- Thanks to OpenAI for providing the GPT models to power the documentation generation.
- Inspiration drawn from modern documentation tools and best practices in software development.

## Adjustments and Improvements

For any feature requests or bug fixes, feel free to open an issue or submit a PR to the repository. Your feedback is valuable in making Turbo-Docs even better!