"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Import the admin module to enable the admin interface.
from django.urls import path, include  # Import path for defining URL patterns and include for referencing other URL configurations.
from rest_framework.schemas import get_schema_view  # Import the function to generate API schema views.
#from rest_framework.documentation import include_docs_urls  # Import the function to include documentation URLs for the API.
#from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


API_TITLE = 'Blog API'  # Define the title for the API documentation.
API_DESCRIPTION = 'A web API for creating and deleting blogs'
#schema_view = get_swagger_view(title = API_TITLE)  # Create a schema view for the API with the title "Blog API".
# The schema view can be used to generate API documentation or provide an OpenAPI schema.
urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the admin interface at the 'admin/' URL.
    path('api/v1/', include('posts.urls')),  # Include the URL patterns defined in the 'posts' app under the 'api/vi/' path.
    path('api-auth/', include('rest_framework.urls')),  # Include the authentication URLs provided by Django REST framework under the 'api-auth/' path.
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),  # Include the URL patterns for user authentication provided by 'rest_auth' under the 'api/v1/rest-auth/' path.
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Include the URL patterns for user registration provided by 'rest_auth' under the 'api/v1/rest-auth/registration/' path.
    #path('docs/', include_docs_urls( title = 'Blog API')),
    #path('schema/', schema_view),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # raw schema
    path('swagger-docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # optional: ReDoc

]
