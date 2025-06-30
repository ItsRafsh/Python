from django import forms
from .models import Aktivitas

class Aktivitasform(forms.ModelForm):
    class Meta:
        model = Aktivitas
        exclude = ['user', 'slug_ak']  
    
        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Your Activity...'
            }),
            'isi': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Deskripsi atau hal menarik beserta keluh kesah yang kamu dapat...'
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600',
                'placeholder': 'Rating dari 1-10'
            }),
            'kategori': forms.Select(attrs={
                'class': 'w-full rounded px-4 py-2 border border-gray-600 appearance-none',
                'style': 'color:white; background-color:#374151;'
            }),
            'hari': forms.Select(attrs={
                'class': 'w-full bg-gray-800 text-white rounded px-4 py-2 border border-gray-600 appearance-none'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(Aktivitasform, self).__init__(*args, **kwargs)
        self.fields['Kategori'].empty_label = "-- Pilih Kategori --"
        self.fields['hari'].choices = [('', '-- Pilih Hari --')] + list(self.fields['hari'].choices)[1:]
        self.fields['rating'].choices = [('', '-- Pilih rating --')] + list(self.fields['rating'].choices)[1:]


