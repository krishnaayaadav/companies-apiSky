
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
import json

f = APIRequestFactory(format='json')
url = "http://127.0.0.1:8000/api/company/"
temp_url = 'http://127.0.0.1:8000/api/company/10/'



class CompanyTester(APITestCase):
   
   def test_all_comp_data(self):
      """testing all companies data"""
      r = self.client.get(url)
      return self.assertEqual(r.status_code, 200)
   
   def test_single_comp_data(self):
      r = self.client.get(temp_url)
      self.assertEquals(r.status_code, 200)
      
   def test_insertion(self):
      data = {
            'comp_name': "My XYZ Company",
            "comp_headq": 'Delhi',
            "how_old":  '2+ years',
            "comp_no_emp": '10 lacks',
            "comp_review": '4.5',
            "open_jobs": "10",
            "comp_type": 1,
            "comp_services": 'service',
            "comp_desc": 'desc'
         }
      headers = {
         'content-type': 'application/json'
      }
      data = json.dumps(data)
      
      r  = self.client.post(url, data=data, headers=headers)
      self.assertEquals(r.status_code, 201)
      
   def test_delete_comp(self):
      r = self.client.delete(temp_url)
      print(r.status_code)
      
      
      
      
      
      
            



