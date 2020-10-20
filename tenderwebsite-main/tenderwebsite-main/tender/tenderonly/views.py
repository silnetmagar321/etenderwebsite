from django.http import Http404
from django.shortcuts import render
from tenderapp.models import Tender
from advertise.models import Advertising
from django.contrib.auth.decorators import login_required
from memberships.models import Membership, UserMembership



def all(request):
    tender = Tender.objects.order_by('-created_at')[:3]
    advertise = Advertising.objects.order_by('-timestamp')[:3]

    context = {'tender': tender, 'advertise': advertise}
    template = 'tenderonly/all.html'
    return render(request, template, context)


@login_required
def single(request, slug):
    try:
        tender = Tender.objects.get(slug=slug)
        advertise = Advertising.objects.order_by('-timestamp')[:3]
        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type
        context = {'tender': tender, 'advertise': advertise, 'user_membership_type':user_membership_type}
        template = 'tenderonly/single.html'
        return render(request, template, context)

    except:
        return render(request, 'loginrequired.html')


