from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company

from django.shortcuts import render
from django.views import View


class Documentation(View):
   
   def get(self, request):
      return render(request, 'app/home.html')

class CompanyAPI(viewsets.ModelViewSet):
   
   queryset = Company.objects.all()
   serializer_class = CompanySerializer
   
   