"""digital_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('logout/', views.user_logout, name='logout'),

    path('', include('tenderapp.urls')),
    path('tender/', include('tenderonly.urls')),
    path('auction/', include('auction.urls')),
    path('eoi/', include('eoi.urls')),
    path('intent2award/', include('intent2awards.urls')),
    path('others/', include('others.urls')),
    path('proposal/', include('proposal.urls')),
    path('quotation/', include('quotation.urls')),
    path('standing-list/', include('standinglist.urls')),
    path('advertising/', include('advertise.urls'), name='advertising'),

    path('s/', views.search, name='search'),
    path('u/', include('profiles.urls', namespace='profiles')),

    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
    path('contact-us/', views.ContactUs.as_view(), name='contactus'),
    path('pricing/', views.Pricing.as_view(), name='pricing'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('team/', views.Team.as_view(), name='team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)