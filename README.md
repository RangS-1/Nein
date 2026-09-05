<div align="center">
<a href="github.com/RangS-1/Nein">
<img src="src/nein/icon.ico" alt="Nein Icon"/>
</a>

# Nein

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.0-red?logo=windows&logoColor=white)](https://github.com/RangS-1/Nein)

</div>

**Nein** is a simple text editor inspired by **nano**, designed specifically to run on **Windows** using the CMD terminal (I don't know if it can also run in PowerShell). I believe that as a developer, once your project is finished, you close your text editor and run the project in the terminal, but then you need to make a small change and end up reopening the editor and running it again. It is somewhat frustrating as a developer -_-.

> **Important note**: This project is still in its early development stage (**uncompleted**). Many features have not yet been implemented, and there may still be many bugs. Please contribute if you want to add new features.

## Features

- Open text files
- Display file contents
- Basic keyboard navigation
- Nano-like interface (simple footer)

## Unfinished goals

- Search text (`Ctrl+W`)
- Cut, copy, and paste lines
- Simple undo
- Syntax highlighting

## Installation and usage

```Python
git clone https://github.com/RangS-1/Nein.git
cd Nein
python -m venv venv
cd venv/Scripts
activate
cd Projects
pip install -r requirements.txt
python nein.py filename.txt
```


## Contribution

This project is very open to contributions, especially in:
- Adding new features
- A more unique/interesting UI than Nano

## License

This project is licensed under the [MIT](LICENSE) - see the [LICENSE](LICENSE) file for details.