from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name', \
        widget=forms.TextInput(attrs={'class':'form-contol'}))
    mail = forms.CharField(label='mail', \
        widget=forms.TextInput(attrs={'class':'from-control'}))
    age = forms.IntegerField(label='age', \
        widget=forms.NumberInput(attrs={'class':'from-control'}))
