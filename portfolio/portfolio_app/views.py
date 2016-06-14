from django.shortcuts import HttpResponse
from django.views.generic import View
from portfolio_app.forms import ContactForm
from django.core import mail

# Create your views here.


from django.views.generic import TemplateView
from portfolio_app.models import About, Portfolio, Education, Experience
# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from .forms import UserForm, ProfileForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse_lazy


class ClassView(TemplateView):
    """Home page template."""

    template_name = 'index.html'

    def get_context_data(self):
        """Pass image to the homepage."""
        about = About.objects.all()
        portfolio = Portfolio.objects.all()
        education = Education.objects.all()
        experience = Experience.objects.all()
        return {'about': about, 'portfolio': portfolio, 'education': education, 'experience': experience}


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
                form.cleaned_data['message'],
            )
            connection = mail.get_connection()
            email = mail.EmailMessage(
                'New form',
                message,
                'mibrah04@gmail.com',
                'mibrah04@gmail.com'.split(),
                connection=connection
            )
            email.send()
            return HttpResponse('success|<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert"><i class="ion-ios-close-empty"></i></button>Thank you! I will contact you shortly.</div>')
        else:
            return HttpResponse('error|<div class="alert alert-danger"><button type="button" class="close" data-dismiss="alert"><i class="ion-ios-close-empty"></i></button>Please fill the all required fields.</div>')
