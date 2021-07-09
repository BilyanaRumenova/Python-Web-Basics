from django import forms

from phones_media_files.phones.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'
