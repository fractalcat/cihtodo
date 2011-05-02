from django import forms

class AdhocTodoForm(forms.Form):
    name = forms.CharField(max_length=300)

class NoteForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    text = forms.CharField(max_length=500, widget=forms.Textarea)
