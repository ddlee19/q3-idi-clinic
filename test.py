import unittest
import requests
import pandas as pd

# Example From: https://docs.python.org/3/library/unittest.html

class TestBrandInfo(unittest.TestCase):
    # Get brands returns correct number of brands
    def test_get_brands(self):
        val_true = 8
        test_url = 'http://0.0.0.0:5000/api/v1.0/brands'.format(id)
        r = requests.get(test_url)
        test_data = r.json()
        val_test = len(test_data)
        self.assertEqual(val_test, val_true)

    # Mean risk current
    def test_mean_risk_current(self):
        id = 5
        test_url = 'http://0.0.0.0:5000/api/v1.0/brands/{}'.format(id)
        r = requests.get(test_url)
        test_data = r.json()
        val_test = test_data['avg_stats']['risk_score_current']['mean']
        true_data = pd.read_csv('./data/bigtable.csv')
        val_true = true_data[true_data['brandid']==id]['risk_score_current'].mean()
        self.assertEqual(val_test, val_true)

    # Mill count
    def test_brand_mill_count(self):
        id = 3
        test_url = 'http://0.0.0.0:5000/api/v1.0/brands/{}'.format(id)
        r = requests.get(test_url)
        test_data = r.json()
        val_test = test_data['mill_count']
        true_data = pd.read_csv('./data/bigtable.csv')
        val_true = true_data[true_data['brandid']==id]['umlid'].count()
        self.assertEqual(val_test, val_true)

    # 404 error
    def test_brand_404_error(self):
        id = 25
        test_url = 'http://0.0.0.0:5000/api/v1.0/brands/{}'.format(id)
        r = requests.get(test_url)
        val_test = r.status_code
        val_true = 404
        self.assertEqual(val_test, val_true)


if __name__ == '__main__':
    unittest.main()
