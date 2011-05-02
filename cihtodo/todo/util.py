from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from rxp import rxp
from models import *

def do_render(req, tmpl, context):
    return render_to_response(tmpl, context, context_instance=RequestContext(req))

def mark_done(todo):
    todo.done = True
    todo.save()
    if todo.parent:
        if not todo.parent.children.filter(done=False).count():
            mark_done(todo.parent)

def check_done(todo):
    if todo.parent:
        todo.parent.done = False
        todo.parent.save()
        check_done(todo.parent)

def extract_tags(s):
    return set(rxp['tags'].findall(s))

def do_tag(todo, tagname):
    tag, isnew = Tag.objects.get_or_create(name=tagname)
    todo.tags.add(tag)
    tag.count += 1
    tag.save()
    todo.save()

def del_todo(todo):
    for tag in todo.tags.all():
        tag.count -= 1
        tag.save()
    todo.delete()

