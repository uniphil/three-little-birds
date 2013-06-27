import requests
from django import forms
import mailchimp
from mailchimp.chimpy.chimpy import ChimpyException

class FormError(Exception):
    pass


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    cc = forms.BooleanField(required=False)
    message = forms.CharField()

    def send(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            sender = self.cleaned_data['email'],
            data = {
                'to': ['uniphil@gmail.com', 'info@threelittlebirdstheband.com'],
                'from': sender,
                'subject': '[TLB Contact Form] message from {}'.format(name),
                'text': self.cleaned_data['message']
            }
            if self.cleaned_data['cc']:
                data['cc'] = sender

            # SEND THAT SHIT
            import os, requests
            mailgun_response = requests.post(
                "https://api.mailgun.net/v2/threelittlebirds.mailgun.org/messages",
                auth=('api', os.environ.get('MAILGUN_API_KEY')),
                data=data,
            )
            if mailgun_response.status_code != 200:
                #return HttpResponse('uh oh, {} {}'.format(mailgun_response.status_code, mailgun_response.text))
                raise FormError('bad response from mailgun: {}'
                                .format(mailgun_response.status_code))


class NewsletterForm(forms.Form):
    nemail = forms.EmailField(required=True)

    def subscribe(self):
        if self.is_valid():
            email = self.cleaned_data['nemail']

            try:
                mc_con = mailchimp.utils.get_connection()
                mc_list = mc_con.get_list_by_id('3c408de96f')
                mc_list.subscribe(email, {'EMAIL': email})
            except ChimpyException:
                raise FormError('already subscribed?')
