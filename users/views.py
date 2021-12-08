from django.shortcuts import reverse, get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
import secrets
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import get_template
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from users.forms import RegisterForm, PasswordForm, ProfileImageForm
from users.models import Activation
from users.email import send_activation_email
from utils.constants.activation import ACTIVATION_DICT


AuthUserModel = get_user_model()


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('email')  # 'username' is a mandatory parameter name for authenticate()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Login failed, please try again.')

            return render(request, 'users/login.html', {})
        else:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')

            return redirect('/')

    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")

    return redirect('/')


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, "An email has been sent to your inbox, please use the link to activate your account.")

            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })


def activate(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.expires_at < timezone.now():
        return redirect(reverse('users:regenerate_token', args=(token,)))

    if request.method == 'GET':
        form = PasswordForm(activation.user)
    else:
        form = PasswordForm(activation.user, request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Account activated successfully, you can now login.')

            return redirect(reverse('users:login'))

    return render(request, 'users/email/set_password.html', {
        'form': form,
        'token': token,
    })


def regenerate_token(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.expires_at >= timezone.now():
        redirect('users:activate', args=(token, ))

    activation.token = secrets.token_hex(32)
    activation.expires_at = timezone.now() + timezone.timedelta(**ACTIVATION_DICT)
    activation.save()

    send_activation_email(activation)
    messages.info(request, f'A new email has been sent to {activation.user}, '
                           f'follow those instructions to activate your account.')

    return redirect('/')


@login_required
def show_profile(request):
    if request.method == 'GET':
        form = ProfileImageForm()
    else:
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form,
    })


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = AuthUserModel.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'

                    context = {
                        'email': user.email,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'domain': f'{settings.LOCALHOST_DOMAIN}',
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    template = get_template('users/email/password_reset_email.html')
                    content = template.render(context)

                    email = EmailMultiAlternatives(
                        subject=subject,
                        body=content,
                        to=[user.email],
                    )
                    email.content_subtype = 'html'
                    email.send()
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')

                    return redirect('done/')

                messages.error(request, 'An invalid email has been entered.')

    password_reset_form = PasswordResetForm()

    return render(request=request, template_name='users/password_reset.html',
                  context={'password_reset_form': password_reset_form})
