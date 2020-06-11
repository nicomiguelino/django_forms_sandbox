from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .forms import ContactForm

class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')

class Example01(View):
    """Using the Form class to render HTML forms in templates."""
    def get(self, request):
        contact_form = ContactForm()

        return render(request, 'main/example_01.html', {
            'contact_form': contact_form
        })

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            sender = contact_form.cleaned_data['sender']
            cc_myself = contact_form.cleaned_data['cc_myself']

            recipients = ['info@example.com']

            if cc_myself:
                recipients.append(sender)

            context = {}
            request.session.update(contact_form.cleaned_data)
            request.session.update({ 'recipients': recipients })

            return redirect(reverse('main:index'))
