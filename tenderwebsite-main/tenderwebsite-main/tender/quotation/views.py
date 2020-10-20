from django.http import Http404
from django.shortcuts import render
from .models import Quotation
from memberships.models import Membership, UserMembership


def all(request):
    auction = Quotation.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'quotation/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Quotation.objects.get(slug=slug)
        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type

        context = {'tender': auction, 'user_membership_type':user_membership_type}
        template = 'quotation/single.html'
        return render(request, template, context)

    except:
        return render(request, 'loginrequired.html')

