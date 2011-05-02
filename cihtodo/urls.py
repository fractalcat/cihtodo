from django.conf.urls.defaults import *
import todo.urls

urlpatterns = patterns('',
    (r'', include(todo.urls)),
)
