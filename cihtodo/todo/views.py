from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import *
from util import *
from forms import *

def show_tag(req, tagname):
    try:
        tag = Tag.objects.get(name=tagname)
    except Tag.DoesNotExist:
        tag = None
    active = tag.todos.filter(done=False) if tag else []
    done = tag.todos.filter(done=True) if tag else []
    return do_render(req, 'showtag.html', {
        'active' : active,
        'done' : done,
        'tag' : tagname,
    })

def list_tags(req):
    tags = Tag.objects.all()
    return do_render(req, 'tags.html', {'tags' : tags})

def adhoc_show(req, pk):
    active = []
    done = []
    todo = None
    form = AdhocTodoForm()
    noteform = NoteForm()
    if int(pk) != 0:
        todo = get_object_or_404(AdhocTodo, pk=pk)
        active = todo.children.filter(done=False)
        done = todo.children.filter(done=True)
        if todo.parent:
            parent = todo.parent
    else:
        active = AdhocTodo.objects.filter(done=False, parent__isnull=True)
        done = AdhocTodo.objects.filter(done=True, parent__isnull=True)
    return do_render(req, 'todo.html', {
            'active' : active,
            'done' : done,
            'todo' : todo,
            'form' : form,
            'noteform' : noteform,
            }
                     )

def adhoc_todos(req):
    return adhoc_show(req, 0)

def adhoc_add(req, pk):
    try:
        par = AdhocTodo.objects.get(pk=pk)
    except:
        par = None
    if req.method == 'POST':
        form = AdhocTodoForm(req.POST)
        if form.is_valid():
            new = None
            if par:
                new = AdhocTodo(name=form.cleaned_data['name'], parent=par)
            else:
                new = AdhocTodo(name=form.cleaned_data['name'])
            tags = extract_tags(form.cleaned_data['name'])
            new.save()
            for tag in tags:
                do_tag(new, tag)
            check_done(new)
    return HttpResponseRedirect(reverse(adhoc_show, args=(par.pk if par else 0,)))

def add_note(req, pk):
    todo = get_object_or_404(AdhocTodo, pk=pk)
    if req.method == 'POST':
        form = NoteForm(req.POST)
        if form.is_valid():
            note = Note(todo=todo, text=form.cleaned_data['text'])
            if form.cleaned_data.get('name', None):
                note.name = form.cleaned_data['name']
            note.save()
    return HttpResponseRedirect(reverse(adhoc_show, args=(pk,)))

def show_note(req, pk):
    note = get_object_or_404(Note, pk=pk)
    return do_render(req, 'note.html', {'note' : note})

def adhoc_done(req, pk):
    todo = get_object_or_404(AdhocTodo, pk=pk)
    mark_done(todo)
    return HttpResponseRedirect(reverse(adhoc_show, args=(todo.parent.pk if todo.parent else 0,)))

