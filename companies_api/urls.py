
from django.contrib import admin
from django.urls import path,include
from api_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Documentation.as_view(), name='homepage'),
    path('api/', include('api_app.api_urls')),


]
