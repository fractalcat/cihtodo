from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from views import *

class Tag(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-count']

class AdhocTodo(models.Model):
    name = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='todos', blank=True, null=True)
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)

    class Meta:
        ordering = ['created']

    def _get_done_children(self):
        done = 0
        if self.children.all.count():
            done = self.children.all.filter(done=True).count()
        return done

    def _get_pretty(self):
        try:
            tag_url = settings.TODO_TAG_URL
        except AttributeError:
            tag_url = "/t"
        pretty = self.name
        for tag in self.tags.all():
            url = '%s/%s' % (tag_url, tag.name)
            pretty = pretty.replace('#%s' % tag.name, '<a href="%s">#%s</a>' % (
                url,
                tag.name,
            ))
        return pretty 

    n_done = property(_get_done_children)
    pretty = property(_get_pretty)

class Note(models.Model):            
    todo = models.ForeignKey(AdhocTodo, related_name="notes")
    name = models.CharField(max_length=100, blank=True)
    text = models.TextField()

