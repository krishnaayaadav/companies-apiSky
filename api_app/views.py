
from django.shortcuts import render
from django.views import View


class Documentation(View):
   
   def get(self, request):
      return render(request, 'app/home.html')

   