# Which of these do we need to create
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

# This was here by default - not sure if we will need it or not
from django.shortcuts import render

# At least they are using class-based views!
class 'UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_registration.html'

    def get_success_url(self):
        return reverse('home')