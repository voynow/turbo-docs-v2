# Turbo Docs

Welcome to Turbo Docs, a tool designed to effortlessly generate documentation for your Python projects. Leveraging AI capabilities, Turbo Docs can create detailed `README.md` files by analyzing your code base.

## Project Overview

**Name:** Turbo Docs  
**Version:** 2.0.0  
**Description:** Default template for PDM package  
**License:** MIT  
**Author:** Voynow, [voynow99@gmail.com](mailto:voynow99@gmail.com)

## Requirements

Turbo Docs requires Python 3.11 or higher and the following Python packages:

- `tiktoken>=0.9.0`
- `openai>=1.63.2`
- `pydantic>=2.10.6`
- `python-dotenv>=1.0.1`

The project uses PDM as a package manager and build tool.

## Installation

Ensure you have Python 3.11+ installed. You can install Turbo Docs and its dependencies using PDM:

```bash
pdm install
```

## Usage

Turbo Docs provides a CLI to generate documentation. To generate a `README.md` file, run:

```bash
pdm run turbo-docs --readme
```

The CLI will parse your project files and create a comprehensive `README.md` for your project.

## How It Works

The tool scans through your project files, determines the content based on predefined code extensions, and generates descriptive documentation using OpenAI's API. It utilizes:

- An LLM (Language Learning Model) for natural language processing tasks like generating documentation.
- Token counting to manage API requests effectively.

## Development

To contribute or modify Turbo Docs:

1. Clone the repository.
2. Ensure all development dependencies are installed using PDM.
3. The following scripts and settings are available in the project:

### Project Scripts

- `turbo-docs`: Entry point for generating documentation through the command line interface.

### Key Files and Functions

- **`readme.py`**: Contains functions to list project files, convert them to strings, and generate a `README.md` file.
- **`cli.py`**: CLI script for running the document generation process.
- **`llm.py`**: Defines functions to interact with OpenAI's API for generating text completions.

### Code Extensions Supported

Turbo Docs processes files with a variety of extensions including, but not limited to:

- Web (e.g. `.js`, `.html`, `.css`)
- Backend (e.g. `.py`, `.java`)
- Shell scripts (e.g. `.sh`, `.bat`)
- Configuration files (e.g. `.json`, `.yaml`)
- Templates (e.g. `.j2`, `.tpl`)
- Documentation (e.g. `.md`, `.rst`)

### Environment Variables

Make sure you have an OpenAI API Key set in your environment:

```
OPENAI_API_KEY=<your_openai_api_key>
```

## Contributing

Contributions to Turbo Docs are welcome! Please follow the standard Git workflow and submit a pull request. For significant changes, please discuss them with the repository owner first.

## License

Turbo Docs is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For issues, questions, or feature requests, please contact the author at [voynow99@gmail.com](mailto:voynow99@gmail.com).

---

Harness the power of AI to streamline your documentation process with Turbo Docs!