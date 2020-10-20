from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, TemplateView

from django.shortcuts import render
from tenderapp.models import Tender
from auction.models import Auction
from eoi.models import Eoi
from intent2awards.models import Intents2Awards
from others.models import Others
from proposal.models import Proposal
from quotation.models import Quotation
from standinglist.models import StandingList
from django.db.models import Q

class AboutUs(TemplateView):
    template_name = 'aboutus.html'


class ContactUs(TemplateView):
    template_name = 'contactus.html'


class Pricing(TemplateView):
    template_name = 'pricing.html'


class Faq(TemplateView):
    template_name = 'faq.html'


class Team(TemplateView):
    template_name = 'team.html'


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        tender = Tender.objects.filter(
            Q(title__icontains=q, ) |
            Q(service__icontains=q) |
            Q(org_address__icontains=q, org_address__iexact=q)
        )
        auction = Auction.objects.filter(title__icontains=q)
        eoi = Eoi.objects.filter(title__icontains=q)
        intent2awards = Intents2Awards.objects.filter(title__icontains=q)
        others = Others.objects.filter(title__icontains=q)
        proposal = Proposal.objects.filter(title__icontains=q)
        quotation = Quotation.objects.filter(title__icontains=q)
        standinglist = StandingList.objects.filter(title__icontains=q)
        context = {'query': q, 'tender': tender, 'auction': auction, 'eoi': eoi, 'intent2awards': intent2awards, 'others': others,
                   'proposal': proposal, 'quotation': quotation, 'standinglist': standinglist}

        template = 'result.html'
    else:
        template = 'tenderapp/all.html'
        context = {}
    return render(request, template, context)



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('tender:all'))
