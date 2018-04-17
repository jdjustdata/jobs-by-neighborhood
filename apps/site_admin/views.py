# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User

from braces import views


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'site_admin/signup.html'
    views.AnonymousRequiredMixin
    views.FormValidMessageMixin

    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET.get('next')
        return reverse_lazy('business:get_all')
    

class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'site_admin/login.html'
    views.AnonymousRequiredMixin
    views.FormValidMessageMixin

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET.get('next')
        return reverse_lazy('business:get_all')
    
