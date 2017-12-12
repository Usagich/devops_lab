import unittest
import info

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_dict(self):
        '''Check that dictionary is not empty'''
        self.assertTrue(info.pf)

if __name__ == '__main__':
    unittest.main()