from django.shortcuts import HttpResponse
from django.views.generic import View
from sternshus_dummy_app.forms import ContactForm
from django.core import mail
import os

# Create your views here.

class ContactView(View):

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            message = """
            From: {}
            Email: {}
            Message: {}
            """.format(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            connection = mail.get_connection()
            email = mail.EmailMessage(
                'New form',
                message,
                'no-reply@sternshus.com',
                os.environ.get('BOT_TARGET', "no-reply@sternshus.com").split(),
                connection=connection
            )
            email.send()
            return HttpResponse('success|<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert"><i class="ion-ios-close-empty"></i></button>Thank you! We will contact you shortly.</div>')
        else:
            return HttpResponse('error|<div class="alert alert-danger"><button type="button" class="close" data-dismiss="alert"><i class="ion-ios-close-empty"></i></button>Please fill the all required fields.</div>')
