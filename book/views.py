from django.shortcuts import render
from book.forms import UserForm, UserProfileForm, SubscriptionForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from book.models import Subscription, SubscriptionType, PersonEmpowered, UserProfile, Address, Shopkeeper
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Create your views here.
def index(request):
	context_dict = {}
        if request.user:
            context_dict['username'] = request.user.username
	return render(request, 'app/index.html', context_dict)

def history(request):
    context_dict = {}
    return render(request, 'book/history.html', context_dict)

def blogs(request):
    context_dict = {}
    return render(request, 'book/blogs.html', context_dict)

def prices(request):
    context_dict = {}
    return render(request, 'book/prices.html', context_dict)

@login_required
def user_page(request):
	context_dict = {}
        subscription = Subscription.objects.get(user = request.user)
        context_dict['shipments'] = subscription.available_shipments + subscription.extra_shipments
        if subscription.level.name != "Simple":
            context_dict['subscription'] = subscription
        context_dict['persons'] = PersonEmpowered.objects.filter(subscription = subscription)
	return render(request, 'book/user.html', context_dict)

@login_required
def get_shipment(request):
	context_dict = {}
	return render(request, 'book/get_shipment.html', context_dict)

@login_required
def confirmation(request):
    context_dict = {}
    return render(request, 'book/confirmation.html', context_dict)

@login_required
def subscribe_pay(request):
    context_dict = {}
    if request.method == 'POST':
        level = request.POST.get('level')
        saver = request.POST.get('saver')
        subscription_type = SubscriptionType.objects.get(name = level)
        cost = subscription_type.monthly_fee
        if saver:
        	cost += subscription_type.store_shipment_fee
        context_dict['cost'] = cost
        context_dict['level'] = level
    return render(request, 'book/subscribe_pay.html', context_dict)

@login_required
def subscribe(request):
    context_dict = {}
    if request.method == 'POST':
        level = request.POST.get('level')
        subscription_type = SubscriptionType.objects.get(name = level)
        subscription = Subscription.objects.get(user = request.user)
        subscription.level = subscription_type
        subscription.available_shipments = subscription_type.amount_of_shipments
        subscription.save()
    return HttpResponseRedirect('/user_page')

def account(request):
	context_dict = {}
	subscription = Subscription.objects.get(user = request.user)
	context_dict['subscription'] = subscription
	if subscription.level.name == "Platinum":
		context_dict['platinum'] = True
	context_dict['all_shipments'] = subscription.available_shipments + subscription.extra_shipments
	date = subscription.renew_date + relativedelta(months=1)
	context_dict['renew_date'] = date.strftime('%d/%m/%Y')
	return render(request, 'app/account.html', context_dict)

def add_address(request):
	context_dict = {}
	subscription = Subscription.objects.get(user = request.user)
	shopkeepers = Shopkeeper.objects.all()
	addresses = Address.objects.filter(subscription = subscription)
	context_dict['addresses'] = addresses
	context_dict['shopkeepers'] = shopkeepers
	if len(addresses) < subscription.level.amount_of_addresses:
		context_dict['full'] = False
	else:
		context_dict['full'] = True
	return render(request, 'app/add_address.html', context_dict)

def registration_subscription(request):
    context_dict = {}
    if request.method == 'POST':
        selected_plan = request.POST['plan']
        subscription_type = SubscriptionType.objects.get(name = selected_plan)
        subscription = Subscription()
        subscription.user = request.user
        subscription.level = subscription_type
        subscription.available_shipments = subscription_type.amount_of_shipments
        if selected_plan == "Gold":
            subscription.first_addressee_name = request.POST.get('firstname')
            subscription.first_addressee_phone = request.POST.get('firstphone')
            subscription.saver = request.POST.get('saver')
        elif selected_plan == "Platinum":
            subscription.first_addressee_name = request.POST.get('firstname')
            subscription.first_addressee_phone = request.POST.get('firstphone')
            subscription.second_addressee_name = request.POST.get('secondname')
            subscription.second_addressee_phone = request.POST.get('secondphone')
        elif selected_plan == "Silver":
        	subscription.saver = request.POST.get('saver')
        subscription.save()
        context_dict['subscription'] = subscription
    return HttpResponseRedirect('/account')

@login_required
def add_person(request):
    context_dict = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        subscription = Subscription.objects.get(user = request.user)
        person = PersonEmpowered(name = name, surname = surname, phone = phone, subscription = subscription)
        person.save()
    return HttpResponseRedirect('/user_page')

@login_required
def pay(request):
	context_dict = {}
	if request.method == 'POST':
		level = SubscriptionType.objects.get(pk=4)
        subscription = Subscription.objects.get(user = request.user)
        if subscription:
            subscription.extra_shipments += 1
            subscription.save()
        else:
    		subscription = Subscription(user = request.user, available_shipments = 0, extra_shipments = 1, level = level)
    		subscription.save()
	return render(request, 'book/confirmation.html', context_dict)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.phone = request.POST.get('phone')
            user_profile.save()
            registered = True
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            login(request, user)
            return render(request, 'app/package.html', {'user': user})
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render(request,
            'app/register.html',
            {'user_form': user_form, 'user_profile_form': user_profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/account')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'app/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')