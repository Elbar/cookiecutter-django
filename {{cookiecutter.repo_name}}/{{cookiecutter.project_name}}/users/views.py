# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import ListView
from braces.views import LoginRequiredMixin
from .forms import UserForm
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User


class UserListView(LoginRequiredMixin, ListView):
    model = User
