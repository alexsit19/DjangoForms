from django import forms

class IncrementForm(forms.Form):
    number = forms.DecimalField(widget=forms.NumberInput({'cols' : 80}))

