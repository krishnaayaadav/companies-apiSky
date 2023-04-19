
from api_app.models import Types,Company
from .serializers import CompanySerializer
from django.test import TestCase,Client

client = Client()

from django.urls import reverse
from rest_framework import status

get_post = 'get_and_post_api'
update_delete = 'detail_update_delete_api'
url = 'http://127.0.0.1:8000/api/companies/'


import json,random

class CompanyModelTest(TestCase):
   """Here we are testing model operation(without api) companies creation,updation,deletion and details-page"""
   
   
   def setUp(self):
      # inilizing of new obj comp
      self.comp_type = Types.objects.create(name='Private')
      
      # comp obj creation
      self.comp = Company.objects.create(comp_name= "Pandits ",
            comp_type = self.comp_type,
            comp_headq= "Mumbia",
            how_old= "1",
            comp_no_emp= "dfdf",
            comp_review="sdf",
            open_jobs="df",
            comp_services= "df",
            comp_desc= "lkdf")
      
      self.data = {
            "comp_name": "Pandits ",
            "comp_type": "Private",
            "comp_headq": "Mumbia",
            "how_old": "1",
            "comp_no_emp": "dfdf",
            "comp_review": "sdf",
            "open_jobs": "df",
            "comp_services": "df",
            "comp_desc": "lkdf"
      }
      
  
   # creation test
   def test_comp_creation(self):
      """checking weather data inserting in db smoothly"""
      
      nm  = self.data['comp_name']
      comp = self.comp
      
      # check comp name
      self.assertEqual(comp.comp_name, nm)
      
      # check comp type
      self.assertEqual(comp.comp_type, self.comp_type)
      
      # checking no of emp
      self.assertEqual(comp.comp_no_emp, self.data['comp_no_emp'])
      
      
      print('\n obj created successfuly')
   
   # checking single company
   
   def test_comp_detail(self):
      comp = self.comp
      
      print(f'\nCompany details: {comp.comp_name} {comp.comp_desc}')
      
      self.assertEqual(self.data['comp_no_emp'], comp.comp_no_emp)
   
   def test_comp_updation(self):
      comp = self.comp
      
      comp.comp_name = "TCS"
      comp.save()
      
      self.assertEqual(comp.comp_name, 'TCS')
      
   def test_comp_deletion(self):
      
      comp = Company.objects.all()
      name = self.comp.comp_name
      self.comp.delete()
      
      try:
        comp = Company.objects.get(comp_name=name)  
      except:
         comp = True
      else:
         comp = False
      
        
   # checking weather obj does not exist     
      self.assertEqual(comp, True)
      
      
      
   
      
      
      
      
   # def test_get_comp(self):
   #    all_cmp = Company.objects.all()
      
class CompanyAPIsTest(TestCase):
   
   def setUp(self):
      self.type1 = Types.objects.create(name='Private')
      self.type2 = Types.objects.create(name='Public')
      
      # creating objs comp
      for i in range(10):
         self.comp = Company.objects.create(comp_name= f"Pandits {i}",
            comp_type = random.choice([self.type1, self.type2]),
            comp_headq= "Mumbia",
            how_old= "1",
            comp_no_emp= "dfdf",
            comp_review="sdf",
            open_jobs="df",
            comp_services= "df",
            comp_desc= "lkdf")
      
      comp = Company.objects.filter(comp_type=self.type1)[0]
      self.pk = comp.pk 
   
   def test_comp_list_data(self):
      """testing comp list api"""
      
      # we are making request
      response = self.client.get(reverse(get_post)) 
      # response = self.client.get(url)
      
      # print(response.data, response.status_code, type(response.data))
      
      all_comp = Company.objects.all().order_by('-pk')
      serializer = CompanySerializer(all_comp, many=True)
      
      # checking comp count
      self.assertGreaterEqual(all_comp.count(), 10)
      
      
      # print(type(response.content), type(serializer.data))
      
      # checking response data is equal to our db data or not
      self.assertEqual(serializer.data, response.data)
      
      print('\n getting all data well')
      
   def test_single_comp_obj(self):
      comp = Company.objects.filter(comp_type=self.type1)[0]
      pk = comp.pk 
      
      # make req
      response = client.get(reverse(update_delete, kwargs={'id': pk}))
      
      # print(response.status_code, response.data)
      
      obj = Company.objects.get(pk=pk)
      serializer = CompanySerializer(obj)
      
      # checking reponse data
      self.assertEqual(response.data, serializer.data)
      
      # self.assertEqual(response.data)
      
      # print(response.data['pk'])
      
      self.assertEqual(response.data['pk'], obj.pk)
      
      # chekcing status code
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      
   def test_invalid_single_page(self):
      
      response = client.get(reverse(update_delete, kwargs={'id': 100}))
      
      # print(response.status_code)
      
      try:
         comp = Company.objects.get(pk=100)
      except:
         comp = None 
      # self.assertEqual(res)
      # print(type(response.data), type(None))
      
      self.assertEqual(response.data, comp)
      
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
      
   def test_partialy_update(self):
      """testing patch request here"""
      
      response = client.patch(reverse(update_delete, kwargs={'id': self.pk}))
      
      print('response code: ', response.status_code, response.data)
      
      
      
      
      
      