# unity-yaml-normalize

[![PyPI version](https://badge.fury.io/py/unity-yaml-normalize.svg)](https://badge.fury.io/py/unity-yaml-normalize)
[![Python Versions](https://img.shields.io/pypi/pyversions/wandbox_api.svg)](https://pypi.org/project/unity-yaml-normalize/)

Normalize and overwrite Unity YAML files(onfigurations, prefabs, scenes, serialized data, etc) entries.
Implemented by [unity-yaml-parser](https://github.com/socialpoint-labs/unity-yaml-parser), thx!

* Sort entries member
* Normalize negative zero.

## Install

> pip install unity-yaml-normalize

## Usage

```sh
usage: unity-yaml-normalize [-h] [-v] [-o OUTPUT] INPUT

positional arguments:
  INPUT                 input file

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -o OUTPUT, --output OUTPUT
                        output file path
```

e.g.

> unity-yaml-normalize sample/SampleScene.unity -o tmp/SampleScene.unitysample/SampleScene.unity -o tmp/SampleScene.unity

![Example Diff](https://user-images.githubusercontent.com/1439172/115989756-dfcb9400-a5fa-11eb-8fbe-ad9f522e9c5b.png)
