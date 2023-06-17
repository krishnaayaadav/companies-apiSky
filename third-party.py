
import csv, json
import requests, time

def data_insertion(file):
   with open(file=file) as file:
      csv_data = csv.DictReader(file)
      
      url = 'http://127.0.0.1:8000/api/company/'
      
      for comp in csv_data:
         # data insertion from csv file
         typ  = comp['comp_type']
         types = 1
         if typ == 'Private':
            types  = 2
         name = comp['comp_name']
         headq  = comp['comp_headq']
         old  = comp['how_old']
         no_emp  = comp['comp_no_emp']
         reviews  = comp['comp_review']
         service  = comp['comp_services']
         desc  = comp['comp_description']
         
                  
         data = {
            'comp_name': name,
            "comp_headq": headq,
            "how_old":  old,
            "comp_no_emp": no_emp,
            "comp_review": reviews,
            "open_jobs": "10",
            "comp_type": types,
            "comp_services": service,
            "comp_desc": desc
         }

         headers = {
            'content-type': 'application/json'
         }
         data = json.dumps(data)
         r = requests.post(url=url,data=data, headers=headers)
         
         time.sleep(3)
         print(r.json())



def post_emp_data(file):
   # url = 'http://127.0.0.1:8000/api/company/'
   url = 'http://127.0.0.1:8000/api/company/'


   response = requests.post(headers='application/json')

   print(response.json(), )



file = 'companies_list.csv'   
post_emp_data(file)

# data_insertion(file)

# data = {
#    'comp_name': "tcs",
#    "comp_headq": "Mumbai",
#    "how_old":  "20",
#    "comp_no_emp": "50",
#    "comp_review": "df",
#    "open_jobs": "10",
#    "comp_type": 1,
#    "comp_services": "software solutions",
#    "comp_desc": "some description"
# }

# headers = {
#    'content-type': 'application/json'
# }
# data = json.dumps(data)
# r = requests.post(url=url,data=data, headers=headers)


# res = r.json()

# print(res, r.status_code)