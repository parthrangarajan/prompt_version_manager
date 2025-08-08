# prompt-version-manager

[![PyPI version](https://img.shields.io/pypi/v/prompt-version-manager.svg)](https://pypi.org/project/prompt-version-manager/)
[![License](https://img.shields.io/github/license/parthrangarajan/prompt_version_manager.svg)](LICENSE)

A lightweight Python package to automatically track and save versions of prompts. It records all changes to the `prompt` variable, storing each version with a timestamp and optional output in a JSON file.

## Features

- Automatically saves every change to your `prompt` variable with a timestamp.
- Optionally records output associated with the prompt.
- Maintains a history of versions in a single JSON file (`prompt_version_manager.json`).
- Simple and intuitive API using Python properties.
- Pure Python implementation, easy to integrate.

## Installation

Install from PyPI with pip:

pip install prompt-version-manager

text

## Usage

from prompt_version_manager import PromptVersionManager

pvm = PromptVersionManager()

Setting a prompt automatically saves it with the current timestamp
pvm.prompt = "Write a poem about AI."

Optionally save the output related to the prompt
pvm.output = "AI is transforming the world with technology."

text

This creates or updates a `prompt_version_manager.json` file in your working directory containing your prompt history.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Parth Rangarajan  
GitHub: [parthrangarajan](https://github.com/parthrangarajan)
