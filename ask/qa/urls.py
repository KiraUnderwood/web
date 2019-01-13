from django.conf.urls import url
from . import views
from qa.views import one_question


urlpatterns = [
  url(r'^$(?P<num>\d+/$)', one_question),
]
