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

from qa.views import recent, popular, Seequestion, ask_me, login_view, signup_view

"""urlpatterns = [
    url(r'^(?P<num>\d+)/$', question),
]
"""

urlpatterns = [
    url(r'^$', recent),
    url(r'^login/', login_view),
    url(r'^signup/', signup_view),
    url(r'^question/', include('qa.urls')),
    ##url(r'^question/', include('qa.urls')),
    url(r'^ask/', ask_me),
    url(r'^popular/', popular),

  
 
    url(r'^new/', include('qa.urls')),
     

]
