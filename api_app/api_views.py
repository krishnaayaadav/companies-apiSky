from rest_framework import status 
from rest_framework.response import Response
from .serializers import CompanySerializer
from rest_framework.views import APIView
from .models import Company

ok_response = status.HTTP_200_OK
bad_request = status.HTTP_400_BAD_REQUEST
not_found   = status.HTTP_404_NOT_FOUND
created     = status.HTTP_201_CREATED
no_content  = status.HTTP_204_NO_CONTENT

class CompanyAPI(APIView):
   """This will accept only get and post.
      Note: It will take any url paramenters.
      Request allowed: [GET, POST]
      Note: it will not take any url parameter
   """
   
   def get(self, request, format=None):
      """get request to fetch all company list of data"""
      all_comp = Company.objects.all().order_by('-pk')
      serializer = CompanySerializer(all_comp, many=True)
      return Response(serializer.data,ok_response)
   
   def post(self, request, format=None):
      """post request to insert new data into our database"""
      serializer = CompanySerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=created)
      else:
         return Response(serializer.errors, bad_request)
      
class CompaniesAPI(APIView):
   
   """This will provide detial of company, updation and deletion enpoints.
      Request allowed: [GET, PATCH, PUT, DELETE]
      URL parameter is required as pk means primary_key of company
   """
   
   def get(self, request, id, format=None):
      """Details Page for company"""
      if not id:
         error = {'error': 'Id is required'}
         return Response(error, status=bad_request)
      else:
         
         try: 
            comp_data = Company.objects.get(pk=id)
         except:
            return Response(status=not_found)
         else:
            serializer = CompanySerializer(comp_data)
            return Response(serializer.data, status=ok_response)
      
   def patch(self, request, id, format=None):
      """PATCH request for partial updation"""
      try: 
         comp_data = Company.objects.get(pk=id)
      except:
         return Response(status=not_found)
      else:
         serializer = CompanySerializer(comp_data, data=request.data, partial=True, context={'patch': request.method, 'id': id})
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=ok_response)
         else:
            return Response(serializer.errors, status=bad_request)
         
   def put(self, request, id, format=None):
      """PUT request for complete updation"""
      try: 
         comp_data = Company.objects.get(pk=id)
      except:
         return Response(status=not_found)
      else:
         serializer = CompanySerializer(comp_data, data=request.data, context={'put': request.method, 'id': id})
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=ok_response)
         else:
            return Response(serializer.errors, status=bad_request)
         
   def delete(self, request, id, format=None):
      """Delete request for delete company"""
      if not id:
         error = {'error': 'Id is required'}
         return Response(error, status=bad_request)
      else:
         
         try: 
            comp_data = Company.objects.get(pk=id)
         except:
            return Response(status=not_found)
         else:
            comp_data.delete()
            msg = {"msg": "Companies data deleted succefully"}
            return Response(msg, status=no_content)
     