from django import forms

class CreateNewPost(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    content = forms.CharField(label="Content", max_length=500)
    foto_1 = forms.ImageField(label="Sebelum")
    foto_2 = forms.ImageField(label="Sesudah")
