[![Build Status](https://travis-ci.org/blatinier/pyhunspell.png)](https://travis-ci.org/blatinier/pyhunspell)

# About PyHunSpell

**pyhunspell** is a set of Python bindings for the Hunspell spellchecker
engine. It lets developers load Hunspell dictionaries, check words, get
suggestions, add new words, etc. It also provides some basic morphological
analysis related methods.

# Installation

Make sure that `python-dev` and `libhunspell-dev` are installed.

You can install this package using pip:

```
pip install hunspell
```

Or from source using the following command as root:

```
python setup.py install
```

# Usage
```
>>> import hunspell
>>> hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
>>> hobj.spell('spookie')
False
>>> hobj.suggest('spookie')
['spookier', 'spookiness', 'spook', 'cookie', 'bookie', 'Spokane', 'spoken']
>>> hobj.spell('spooky')
True
>>> hobj.analyze('linked')
[' st:linked', ' st:link fl:D']
>>> hobj.stem('linked')
['linked', 'link']
```

# License

PyHunspell itself is licensed under the LGPL version 3 or later, see
lgpl-3.0.txt and gpl-3.0.txt. The files in the debian/ directory and setup.py
are licensed under the GPL version 3.
