"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from pybo.views import IndexView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', IndexView.as_view(), name='index'),  # '/' 에 해당되는 path
    #http://localhost:8000/accounts/login/?next=/pybo/question/create/
    #path('accounts/', include('common.urls')),    # 로그인 URL

]
