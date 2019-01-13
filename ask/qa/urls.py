from django.conf.urls import url
from . import views
from qa.views import most_popular_q


urlpatterns = [
  url(r'^$(?P<num>\d+/$)', one_question),
]
