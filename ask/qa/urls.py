from django.conf.urls import url
from . import views
from qa.views import question


urlpatterns = [
  url(r'^$(?P<num>\d+/$)', question),
]
