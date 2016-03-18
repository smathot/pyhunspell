[![Build Status](https://travis-ci.org/blatinier/pyhunspell.png)](https://travis-ci.org/blatinier/pyhunspell)

# About PyHunSpell

**pyhunspell** is a set of Python bindings for the Hunspell spellchecker
engine. It lets developers load Hunspell dictionaries, check words, get
suggestions, add new words, etc. It also provides some basic morphological
analysis related methods.

See [ChangeLog](https://github.com/blatinier/pyhunspell/blob/master/CHANGELOG.md) for activity.

See [Authors](https://github.com/blatinier/pyhunspell/blob/master/AUTHORS.md) for all contributors.

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

For windows7 [@tallforasmurf](https://github.com/tallforasmurf) compiled a python 3.4 compatible version of the pyhunspell==0.3.3 package available here: http://pyhunspell.latinier.fr
(Warning: Those windows compiled packages are not reviewed or tested). It could work for other windows version or python versions.

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
>>> hobj.spell('spookie')
False
>>> hobj.add('spookie')
>>> hobj.spell('spookie')
True
>>> hobj.remove('spookie')
>>> hobj.spell('spookie')
False
```

# Misc

For information, version naming (introduced for 0.4.0) is based on Hungarian cities ordered by population except Budapest.
The reason why is that hunspell stands for Hungarian Spell.

# License

PyHunspell itself is licensed under the LGPL version 3 or later, see
lgpl-3.0.txt and gpl-3.0.txt. The files in the debian/ directory and setup.py
are licensed under the GPL version 3.
