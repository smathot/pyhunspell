import os
import unittest
from hunspell import HunSpell


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
                         [b'dog', b'pg', b'deg', b'dig', b'dpt',
                          b'dug', b'mpg', b'd pg', b'GDP',
                          b'DP', b'PG', b'DTP', b'dip'])
        self.assertEqual(self.hunspell.suggest('spookie'),
                         [b'spookier', b'spookiness', b'spook', b'cookie',
                          b'bookie', b'Spokane', b'spoken'])

    def test_hunspell_stem(self):
        self.assertEqual(self.hunspell.stem('dog'), [b'dog'])
        self.assertEqual(self.hunspell.stem('permanently'), [b'permanent'])
        self.assertEqual(self.hunspell.stem('linked'), [b'linked', b'link'])

    def test_analyze(self):
        self.assertEqual(self.hunspell.analyze('linked'),
                         [b' st:linked', b' st:link fl:D'])

    def test_add_remove(self):
        self.assertFalse(self.hunspell.spell('pipo'))
        self.hunspell.add('pipo')
        self.assertTrue(self.hunspell.spell('pipo'))
        self.hunspell.remove('pipo')
        self.assertFalse(self.hunspell.spell('pipo'))


class HunSpellGenerateTest(unittest.TestCase):
    def setUp(self):
        self.hunspell = HunSpell("/usr/share/hunspell/en_GB.dic",
                                 "/usr/share/hunspell/en_GB.aff")

    def test_generate(self):
        self.assertEqual(self.hunspell.generate('boy', 'girls'), [b'boys'])

    def test_generate2(self):
        self.assertEqual(self.hunspell.generate2('boy', 'is:Ns'), [b'boys'])

if __name__ == '__main__':
    unittest.main()
