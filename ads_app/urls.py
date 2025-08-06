from django.urls import path
from . import views

urlpatterns = [
    path ('ads/', views.ads_listing, name = "ads_listing"),
    path ('form/', views.ads_form, name = "ads_form"),
    path ('register/', views.register, name = "register"),
    path ('login/', views.login_view, name = "login"),
    path ('logout/', views.logout_view, name = "logout"),
    path('ads/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('exchange/', views.create_exchange_proposal, name='create_exchange_proposal'),
    path('proposed-ads/', views.proposed_ads, name='proposed_ads'),
    path('proposals/update/<int:proposal_id>/', views.update_proposal_status, name='update_proposal_status'),
]


