from django import forms

class InputForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'http:// or https://'}))
    custom_code = forms.CharField(max_length=10, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Optional'}))

    def clean_url(self):
        url = self.cleaned_data['url']
        return url
