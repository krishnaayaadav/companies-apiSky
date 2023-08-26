
from django.contrib import admin
from django.urls import path,include


from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),

    # api roots
    path('api/', include('api_app.api_urls')),

    # documentation for api
    path('api/schema/', SpectacularAPIView().as_view(), name='schema'),
    path('api/docs/',   SpectacularSwaggerView().as_view(url_name='schema')),



]
