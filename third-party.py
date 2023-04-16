print('hello ')

import csv, json
import requests

def data_insertion(file):
   with open(file=file) as file:
      csv_data = csv.DictReader(file)
      for comp in csv_data:
         name = comp['comp_name']
         typ  = comp['comp_type']
         headq  = comp['comp_headq']
         old  = comp['how_old']
         no_emp  = comp['comp_no_emp']
         reviews  = comp['comp_review']
         service  = comp['comp_services']
         desc  = comp['comp_description']
         print(name, typ, headq, old, no_emp, reviews, service,desc)

   
file = 'companies_list.csv'   
# data_insertion(file)

url = 'http://127.0.0.1:8000/api/company/'
r  = requests.get(url=url)
res = r.json()
print(res)