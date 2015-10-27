import os
import unittest
from hunspell import HunSpell

DICT_DIR = os.path.join(os.path.dirname(__file__), '..', 'dictionaries')


class HunSpellTest(unittest.TestCase):
    def setUp(self):
        self.hunspell = HunSpell("/usr/share/hunspell/en_US.dic",
                                 "/usr/share/hunspell/en_US.aff")

    def tearDown(self):
        try:
            del self.hunspell
        except AttributeError:
            pass

    def test_hunspell_spell(self):
        self.assertFalse(self.hunspell.spell('dpg'))
        self.assertTrue(self.hunspell.spell('dog'))
        self.assertFalse(self.hunspell.spell('spookie'))
        self.assertTrue(self.hunspell.spell('spooky'))

    def test_hunspell_suggest(self):
        self.assertEqual(self.hunspell.suggest('dpg'),
                         ['dog', 'pg', 'deg', 'dig', 'dpt',
                          'dug', 'mpg', 'd pg', 'GDP',
                          'DP', 'PG', 'DTP', 'dip'])
        self.assertEqual(self.hunspell.suggest('spookie'),
                         ['spookier', 'spookiness', 'spook', 'cookie',
                          'bookie', 'Spokane', 'spoken'])

    def test_hunspell_stem(self):
        self.assertEqual(self.hunspell.stem('dog'), ['dog'])
        self.assertEqual(self.hunspell.stem('permanently'), ['permanent'])
        self.assertEqual(self.hunspell.stem('linked'), ['linked', 'link'])

    def test_analyze(self):
        self.assertEqual(self.hunspell.analyze('linked'),
                         [' st:linked', ' st:link fl:D'])

if __name__ == '__main__':
    unittest.main()
