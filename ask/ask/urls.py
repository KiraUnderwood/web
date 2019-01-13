"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from qa.views import most_recent_q, most_popular_q, one_question

"""urlpatterns = [
    url(r'^(?P<num>\d+)/$', question),
]
"""

urlpatterns = [
    url(r'^$', most_recent_q),
    url(r'^login/', include('qa.urls')),
    url(r'^signup/', include('qa.urls')),
    url(r'^question/(?P<num>\d+)/$', one_question),
    url(r'^ask/', include('qa.urls')),
    url(r'^popular/', most_popular_q),

  
 
    url(r'^new/', include('qa.urls')),
     

]
