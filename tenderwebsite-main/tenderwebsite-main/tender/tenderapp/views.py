from django.http import Http404
from django.shortcuts import render
from .models import Tender
from auction.models import Auction
from eoi.models import Eoi
from intent2awards.models import Intents2Awards
from others.models import Others
from proposal.models import Proposal
from quotation.models import Quotation
from standinglist.models import StandingList
from advertise.models import Advertising
from .forms import PricingClientForm
from django.contrib.auth.decorators import login_required
from memberships.models import Membership, UserMembership


def all(request):
    tender = Tender.objects.order_by('-created_at')[:4]
    auction = Auction.objects.order_by('-created_at')[:4]
    eoi = Eoi.objects.order_by('-created_at')[:4]
    intent2awards = Intents2Awards.objects.order_by('-created_at')[:]
    others = Others.objects.order_by('-created_at')[:4]
    proposal = Proposal.objects.order_by('-created_at')[:4]
    quotation = Quotation.objects.order_by('-created_at')[:4]
    standinglist = StandingList.objects.order_by('-created_at')[:4]
    advertise = Advertising.objects.order_by('-timestamp')[:4]
    context = {'tender': tender, 'auction': auction, 'eoi': eoi, 'intent2awards': intent2awards, 'others': others, 'proposal': proposal, 'quotation': quotation, 'standinglist': standinglist, 'advertise': advertise}
    template = 'tenderapp/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        tender = Tender.objects.get(slug=slug)
        advertise = Advertising.objects.order_by('-timestamp')[:3]
        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type
        context = {'tender': tender, 'advertise': advertise, 'user_membership_type':user_membership_type}
        template = 'tenderapp/single.html'
        return render(request, template, context)

    except:
        return render(request, 'loginrequired.html')


def pricing_clients(request):
    form = PricingClientForm()

    if request.method == "POST":
        form = PricingClientForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'thankyou.html')

        else:
            print("Error form INVALID!")

    return render(request, 'tenderapp/pricing_clients.html', {'form': form})

