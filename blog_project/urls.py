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

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the admin interface at the 'admin/' URL.
    path('api/v1/', include('posts.urls')),  # Include the URL patterns defined in the 'posts' app under the 'api/vi/' path.
]
