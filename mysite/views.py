from django.shortcuts import render
from .forms import(
        RegistrationForm,
        AccountAuthenticationForm,
        AccountUpdateform

)



# Create your views here.
def home(request):
    return render(request, "base.html", {})



def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email    = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password = raw_pass)
            login(request, account)
            messages.success(request, "You have been Registered as {}".format(request.user.username))

        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "tw/register.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("home")



def  login_view(request):
    context = {}

    user = request.user

    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form    = AccountAuthenticationForm(request.POST)
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form

    return render(request, "tw/login.html", context)

