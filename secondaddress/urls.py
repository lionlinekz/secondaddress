"""secondaddress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from book import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register', views.register),
    url(r'^login', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^user_page/$', views.user_page, name='user_page'),
    url(r'^get_shipment/$', views.get_shipment, name='get_shipment'),
    url(r'^registration_subscription/$', views.registration_subscription, name='registration_subscription'),
    url(r'^account/$', views.account),
    url(r'^shopkeeper/$', views.shopkeeper),
    url(r'^parcels/$', views.parcels),
    url(r'^take_parcel/$', views.take_parcel),
    url(r'^parcels_taken/$', views.parcels_taken),
    url(r'^buy_shipments/$', views.buy_shipments),
    url(r'^add_address/$', views.add_address),
    url(r'^change_plan/$', views.change_plan),
    url(r'^keep_shipments/$', views.keep_shipments),
    url(r'^add_addressee/$', views.add_addressee),
    url(r'^edit_details/$', views.edit_details),
    url(r'^change_password/$', views.change_password),
    url(r'^confirmation/$', views.confirmation),
    url(r'^subscribe_pay/$', views.subscribe_pay),
    url(r'^subscribe', views.subscribe),
    url(r'^add_person', views.add_person),
    url(r'^history', views.history),
    url(r'^blogs', views.blogs),
    url(r'^prices', views.prices),
    url(r'^pay', views.pay),
    url(r'^$', views.index),
]
