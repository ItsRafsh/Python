from django import forms
from .models import Movie

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['user', 'slug_art']  

        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Judul Movie...'
            }),
            'isi': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Deskripsi atau manfaat movie beserta ilmu yang didapat...'
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Rating dari 1-10'
            }),
            'kategori': forms.Select(attrs={
                'class': 'w-full bg-gray-700 text-white rounded px-4 py-2 border border-gray-600 appearance-none'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(Movieform, self).__init__(*args, **kwargs)
        self.fields['Kategori'].empty_label = "-- Pilih Kategori --"
        self.fields['rating'].choices = [('', '-- Pilih rating --')] + list(self.fields['rating'].choices)[1:]
