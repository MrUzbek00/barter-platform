from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Ad, ExchangeProposal
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, AdForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect("/ads/")
    else:
        form = RegisterForm()

    return render(response, 'ads_app/register.html', {"form": form})

def login_view(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                return redirect('ads_listing')
            else:
                return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
    return render(response, 'ads_app/login.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('ads_listing')

@login_required(login_url='login')
def ads_form(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ads_listing')
    else:
        form = AdForm()
    return render(request, 'ads_app/ad_form.html', {'form': form})


@login_required(login_url='login')
def submit_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ads_listing')
    else:
        form = AdForm()
    return render(request, 'ads_app/ads_listing.html')

@login_required(login_url='login')
def edit_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id, user=request.user)
    if ad.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this ad.")
    
    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ads_listing')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads_app/ad_form.html', {'form': form, 'ad': ad})    

def ads_listing(request):
    ads = Ad.objects.all().order_by('-created_at')

    # Filtering
    keywords = request.GET.get('keywords', '')
    category = request.GET.get('category', '')
    condition = request.GET.get('condition', '')
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))

    if keywords:
        ads = ads.filter(
            Q(title__icontains=keywords) |
            Q(description__icontains=keywords)
        )
    if category:
        ads = ads.filter(category__iexact=category)
    if condition:
        ads = ads.filter(condition__iexact=condition)

    paginator = Paginator(ads, limit)
    ads_page = paginator.get_page(page)

    return render(request, 'ads_app/ads_listing.html', {'ads': ads_page,
    })

@login_required(login_url='login')
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)

    if ad.user == request.user:
        return render(request, 'ads_app/ad_detail.html', {'ad': ad, 'error': "You can't offer exchange on your own ad."})

    user_ads = Ad.objects.filter(user=request.user)

    return render(request, 'ads_app/ad_detail.html', {
        "form":ExchangeProposal(),
        'ad': ad,
        'user_ads': user_ads,

    })

@login_required(login_url='login')
def create_exchange_proposal(request):
    if request.method == "POST":
        sender_ad_id = request.POST.get('sender_ad_id')
        receiver_ad_id = request.POST.get('receiver_ad_id')
        comment = request.POST.get('comment', '')

        ad_sender = get_object_or_404(Ad, id=sender_ad_id, user=request.user)
        ad_receiver = get_object_or_404(Ad, id=receiver_ad_id)

        # Prevent proposing to your own ad
        if ad_sender.user == ad_receiver.user:
            return HttpResponse("You cannot propose an exchange with your own ad.", status=400)

        ExchangeProposal.objects.create(
            ad_sender=ad_sender,
            ad_receiver=ad_receiver,
            comment=comment
        )
        return redirect('ads_listing')

    return HttpResponse("Invalid request", status=405)

@login_required(login_url='login')
def proposed_ads(request):
    proposals = ExchangeProposal.objects.filter(
        Q(ad_sender__user=request.user) | Q(ad_receiver__user=request.user)
    ).order_by('-created_at')

    return render(request, 'ads_app/proposed_ads.html', {'proposals': proposals, "user": request.user})


@login_required(login_url='login')
def update_proposal_status(request, proposal_id):
    proposal = get_object_or_404(ExchangeProposal, id=proposal_id)
    if 'delete' in request.POST:
            proposal.delete()
            return redirect('proposed_ads')
    if request.user != proposal.ad_receiver.user:
        return HttpResponseForbidden("You are not allowed to update this proposal.")

    if request.method == "POST":
        
        new_status = request.POST.get("status")
        if new_status in ["pending", "accepted", "rejected"]:
            proposal.status = new_status
            proposal.save()
    return redirect('proposed_ads')



