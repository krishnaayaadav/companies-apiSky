
from django.contrib import admin
from django.urls import path,include

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),

    # api roots
    path('api/', include('api_app.api_urls')),

    # documentation for api
    path('', include_docs_urls(title='Companies API'))


]
