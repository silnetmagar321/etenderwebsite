from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.http import Http404
from accounts.models import Profile
from memberships.models import Membership, UserMembership


User = get_user_model()


class ProfileDetailView(LoginRequiredMixin, DetailView):

    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    fields = ('address', 'mobile_number')
    model = Profile

