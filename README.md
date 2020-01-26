[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Build Status](https://travis-ci.org/vyahello/upgrade-python-kata.svg?branch=master)](https://travis-ci.org/vyahello/upgrade-python-kata)

![My Codewarrior Profile Badge](https://www.codewars.com/users/vyahello/badges/large)

# Upgrade your python kata

This project is aimed to provide solutions for [codewars](https://www.codewars.com) tasks followed by [kata approach](https://en.wikipedia.org/wiki/Kata_(programming)).
You can use it as a troubleshooting case if you stuck with some exercises to accomplish.

## Tools
- python 3.6, 3.7, 3.8
- [black](https://black.readthedocs.io/en/stable/)
- [pylint](https://www.pylint.org/)
- [xdoctest](https://github.com/Erotemic/xdoctest)

## Usage

Please run following script from the root directory of a project:
```bash
➜ python kata/<level-rank>/<task-name>.py
```

## Development notes

To be able to run unittests please execute command below:
```bash
➜ python -m xdoctest kata
```

### Meta

Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
