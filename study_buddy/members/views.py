from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from study_buddy.members.forms import UserRegistrationForm


def index_no_account(request):
    return render(request, 'index_login_register.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('index no_account')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, Try again...")
            return redirect('login user')

    else:
        return render(request, 'users/sign_in.html')


# def register_user(request):
#     if request.method == 'POST':
#         form = ProfileCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, 'Registration successful!')
#             return redirect('index')
#     else:
#         form = ProfileCreateForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'users/sign_up.html', context)

UserModel = get_user_model()


class UserRegistrationView(CreateView):
    # form_class=UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'users/sign_up.html'

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result
