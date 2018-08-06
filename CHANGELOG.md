# Changelog

## 0.5.4 (???)
### Bug fixes
- Fix a memory leak at instanciation (issue #39 fixed by @Far3t)
- Fix an encoding problem (issue #32)
- Use `include_path` for install

## 0.5.3 (2018-02-02)
### Improvements
- Use only setuptools to build package, allows integration with conda

## 0.5.2 (2018-02-01)
### Bug fixes
- Fix installation on linux broken by 0.5.1

## 0.5.1 (2018-01-31)
### Bug fixes
- Fix Installation fail on OSX (issue #33)

## 0.5.0 (2016-06-30)
### New features
- A binding to `add_dic` allowing to load another dic in a hunspell instance (useful for technical terms, e.g, medical dictionary) (issue #30 & #2)

### Improvements
- **Breaking change**: `suggest` no longer returns a list of bytes. It now returns a list of unicode. (issue #24)
- Add license files in pypi tarball (issue #28)

### Note
- Adding the `add_dic` binding required to rewrite the binding in C++. There should be no change of the lib behavior however.

## 0.4.1 (2016-03-31)
### Improvement
- Exception HunSpellError now exists and is catchable (issue #21)
- [Online documentation](https://github.com/blatinier/pyhunspell/wiki/Documentation)

## 0.4.0 - Debrecen (2016-03-18)
### Bug fixes
- Drop the useless third parameter of generate2 which segfaults if not 0 or 1 (**Breaking change**: generate2 only takes 2 arguments now, not 3)

### Improvements
- Add full documentation to all functions
- Add this great CHANGELOG :)
- Add AUTHORS

## 0.3.5 (2016-03-15)
### Improvements
- Add new dict in travis build to fix generate2 tests (Antoine Fontaine)
- Add links to windows7 binaries in README (Warning: those bin are not tested)

## 0.3.4 (2016-03-02)
### New features
- Ability to compile on Windows7 (Nat Picker)
- Add support for method generate2 (Antoine Fontaine)
- Add Travis-ci
- Add tests

### Improvements
- Minor README update (arunbala)
- Rewrite README to markdown syntax (Marios Zindilis)

## 0.3.3 (2015-05-14)
### Improvements
- Correct README informations (links) and add some basic doc in it.

## 0.3.2 (2014-10-03)
### Improvements
- Setup licensing correctly (Till Maas)

### Bug fixes
- Fixes on python 3 (Mateusz Korniak)
- Fix segfault on python 2

## 0.3.1 (2014-09-16)
### Bug fixes
- Fix some possible segfaults and memory leaks

## 0.3.0 (2014-09-16)
### New features
- Python 3 compatibility (Tillmann Karras and Benjamin Drung)
- Add PKG-INFO

### Improvements
- Clean README and pypi package information regarding new repository

## 0.2.0 (2014-02-06)
### New features
- Add some Debian control files (by Sebastiaan Mathot smathot)

### MISC
- Changing maintainer from Sayamindu Dasgupta to Benoît Latinier

## 0.1.0
- Initial bindings to most of hunspell methods


