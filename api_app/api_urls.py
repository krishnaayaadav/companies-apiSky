from django.urls import path
from . import api_views

urlpatterns = [
   path('companies/', api_views.CompanyAPI.as_view(), name='get_and_post_api'),
   path('companies/<int:id>/', api_views.CompaniesAPI.as_view(), name='detail_update_delete_api'),
   
]