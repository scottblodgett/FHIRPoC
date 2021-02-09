import boto3
from botocore.exceptions import ClientError
import unittest
from secretsmanager import get_secret

class TestSecrets(unittest.TestCase):

    def test_annual(self):
        self.assertEqual(get_secret('us-east-2','FHIRKeys'),{"APIKey":"t2o7CGAVBwf8kxxiBEJwLu3hveH9XbWD"})
        #self.assertRaises(ClientError,get_secret('us-east-1','FHIRKeys'),"")

if __name__ == '__main__':
    unittest.main()        