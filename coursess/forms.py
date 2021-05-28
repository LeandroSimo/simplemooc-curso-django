from django import forms
from django.core.mail import message, send_mail
from django.conf import settings

class ContactCourse(forms.Form):
    
    name = forms.CharField(label='None', max_length=100)
    email = forms.EmailField(label='E-mail')
    messade = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )
    
    def send_email(self, course):
        subject = '[%$] Contato' % course
        message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])