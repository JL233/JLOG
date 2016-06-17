from django import forms
class BlogForm(forms.Form):
    title = forms.CharField(max_length=150)
    category = forms.CharField(max_length=15)
    content = forms.TextField()
    timestamp = forms.DateTimeField()