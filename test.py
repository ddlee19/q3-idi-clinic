import unittest
import requests
import pandas as pd

MILLS_API_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"
UML_QUERY = {'country': 'Indonesia'}

# To-Do: Resolve local host IP address dynamically to avoid use of two variables
BASE_API_URL_MAC = "http://0.0.0.0:5000/api/v1.0"
BASE_API_URL_WINDOWS = "http://localhost:5000/api/v1.0"
BASE_API_URL = BASE_API_URL_WINDOWS

# Comments
# - Can use self.assertTrue(<condition>) in later test cases


class TestBrandInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Reads in the BigTable CSV file into a Pandas DataFrame before
        the unit tests execute.
        '''
        super(TestBrandInfo, cls).setUpClass()
        cls.bigTable = pd.read_csv('./data/bigtable.csv')


    def test_get_brands(self):
        '''
        Assert that the "Brands" API endpoint returns the correct number
        of brands.
        '''
        val_true = 8
        test_url = f"{BASE_API_URL}/brands"
        r = requests.get(test_url)
        test_data = r.json()
        val_test = len(test_data)
        self.assertEqual(val_test, val_true)


    def test_mean_risk_current(self):
        '''
        Assert that the mean risk score of a brand's mills, retrieved from the
        "Brands" API endpoint, matches the expected value.
        '''
        id = 5
        test_url = f"{BASE_API_URL}/brands/{id}"
        r = requests.get(test_url)
        test_data = r.json()
        val_test = test_data['avg_stats']['risk_score_current']['mean']
        true_data = self.bigTable
        val_true = true_data[true_data['brandid']==id]['risk_score_current'].mean()
        self.assertEqual(val_test, val_true)

    # Mill count
    def test_brand_mill_count(self):
        '''
        Asserts that the mill count
        '''
        id = 3
        test_url = f"{BASE_API_URL}/brands/{id}"
        r = requests.get(test_url)
        test_data = r.json()
        val_test = test_data['mill_count']
        true_data = self.bigTable
        val_true = true_data[true_data['brandid']==id]['umlid'].count()
        self.assertEqual(val_test, val_true)

    # 404 error on get brandid
    def test_brand_404_error(self):
        id = 25
        test_url = f"{BASE_API_URL}/brands/{id}"
        r = requests.get(test_url)
        val_test = r.status_code
        val_true = 404
        self.assertEqual(val_test, val_true)

    # Get brands mills
    def test_get_brands_mills(self):
        id = 3
        test_url = f"{BASE_API_URL}/brands/{id}"
        r = requests.get(test_url)
        test_data = r.json()

        # Get mill list
        req = requests.get(MILLS_API_URL, params=UML_QUERY)
        res_json = req.json()
        mills = res_json['features']
        mills_umls = [x["properties"]["id"].lower() for x in mills]

        verification_list = []
        for mill in test_data['mills']:
            verification_list.append(mill['umlid'] in mills_umls)

        val_test = all(verification_list)
        val_true = True
        self.assertEqual(val_test, val_true)

    # 404 error on get millid
    def test_mill_404_error(self):
        id = 'po1000001253'
        test_url = f"{BASE_API_URL}/mills/{id}"
        r = requests.get(test_url)
        val_test = r.status_code
        val_true = 404
        self.assertEqual(val_test, val_true)

    # Get millid test brands
    def test_get_mills_brands(self):
        id = 'po1000001058'
        test_url = f"{BASE_API_URL}/mills/{id}"
        r = requests.get(test_url)
        test_data = r.json()
        val_test = set()
        for brand in test_data['brands']:
            val_test.add(brand['brandid'])

        true_data = self.bigTable
        val_true = set(true_data[true_data['umlid']==id]['brandid'])
        self.assertEqual(val_test, val_true)


    # Get mills
    def test_get_mills(self):
        # Get mill list
        req = requests.get(MILLS_API_URL, params=UML_QUERY)
        res_json = req.json()
        mills = res_json['features']
        true_umls = set([x["properties"]["id"].lower() for x in mills])

        # Get mills from web server
        test_url = f"{BASE_API_URL}/mills"
        r = requests.get(test_url)
        test_data = r.json()

        # Verify that each umlid is in the uml list.
        verification_list = []
        test_umls = [x['properties']['umlid'].lower() in true_umls for x in test_data['features']]

        val_test = all(verification_list)
        val_true = True
        self.assertEqual(val_test, val_true)



if __name__ == '__main__':
    unittest.main()
