from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib import messages
from accounts.forms import SignUpForms


class SignUpView(SuccessMessageMixin, FormView):
    success_url = reverse_lazy('home')
    success_message = 'ثبت نام با موفقیت انجام شد'
    template_name = 'registration/signup.html'
    form_class = SignUpForms
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)
