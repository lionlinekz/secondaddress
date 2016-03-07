from django.shortcuts import render
from book.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from book.models import Subscription, SubscriptionType, PersonEmpowered


# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'book/home.html', context_dict)

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
        context_dict['level'] = request.POST.get('level')
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

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
    # Render the template depending on the context.
    return render(request,
            'book/register.html',
            {'user_form': user_form, 'registered': registered} )


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
                return HttpResponseRedirect('/user_page')
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
        return render(request, 'book/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')