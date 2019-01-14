from django.conf.urls import url
from qa.views import Seequestion

urlpatterns = [
  url(r'^(?P<num>\d+)/$', Seequestion),
]
'''
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('qa.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
'''
