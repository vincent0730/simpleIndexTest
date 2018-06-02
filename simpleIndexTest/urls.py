"""simpleIndexTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

"""  定义如何把URL映射到视图函数上 """
from django.conf.urls import include,url
from django.contrib import admin
from lists import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page),
]


""" 2.X版本自动生成的代码
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(, name='home')
]

from simpleIndexTest import views
from lists import views

urlpatterns = patterns('',
        url(r'^$', 'lists.views.home_page', name='home')

    ) 
            #Examples:
            #url('simpleIndexTest.views.home', name='home'),
            #url(r'^admin/', admin.site.urls),
            

            #url(r'^blog/',include('blog.urls')),

            #url(r'^admin/',include(admin.site.urls)),
"""
