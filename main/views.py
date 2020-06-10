from django.shortcuts import render
from django.views import View
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
