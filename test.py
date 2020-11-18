import unittest
import requests

# Example From: https://docs.python.org/3/library/unittest.html

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestBrandInfo(unittest.TestCase):
    # Mean risk current
    def test_mean_risk_current(self):
        data_test = 
        val_test = requests. # Grab risk score current mean from webserver json
        val_true = # Grab mean risk score current from uniquebrands.csv
        self.assertEqual(val_test, val_true)
    
    # Mill count
    def test_mill_count(self):
        pass
    
    # (Maybe) 404 error 

if __name__ == '__main__':
    unittest.main()