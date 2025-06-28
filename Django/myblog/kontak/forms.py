from django import forms
from .models import KontakModel

# class Kontakform(forms.Form):
#     nama = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     pesan = forms.CharField(widget=forms.Textarea)

class Kontakform(forms.ModelForm):
    class Meta:
        model = KontakModel
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']

        if KontakModel.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Email {email} sudah pernah kirim pesan ')
        return email


