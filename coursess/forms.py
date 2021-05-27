from django import forms


class ContactCourse(forms.Form):
    
    name = forms.CharField(label='None', max_length=100)
    email = forms.EmailField(label='E-mail')
    messade = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )