from django import forms
from .models import Youtube

class Youtubeform(forms.ModelForm):
    class Meta:
        model = Youtube
        exclude = ['user', 'slug_art']  

        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Judul video...'
            }),
            'isi': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Deskripsi atau Link Video beserta ilmu yang didapat...'
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Rating dari 1-10'
            }),
            'kategori': forms.Select(attrs={
                'class': 'w-full rounded px-4 py-2 border border-gray-600 appearance-none',
                'style': 'color:red; background-color:#374151;'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(Youtubeform, self).__init__(*args, **kwargs)
        self.fields['Kategori'].empty_label = "-- Pilih Kategori --"
        self.fields['rating'].choices = [('', '-- Pilih rating --')] + list(self.fields['rating'].choices)[1:]


