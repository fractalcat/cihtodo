from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
                       (r'^$', adhoc_todos),
                       (r'^ta$', list_tags),
                       (r'^t$', tags),
                       (r'^t/(\w+)$', show_tag),
                       (r'^(\d+)/$', adhoc_show),
                       (r'^note/(\d+)/$', show_note),
                       (r'^note/(\d+)/add$', add_note),
                       (r'^(\d+)/add$', adhoc_add),
                       (r'^(\d+)/done$', adhoc_done),
                       (r'^api/tags/.*', tag_autocomplete),
)
