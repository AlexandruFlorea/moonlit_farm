from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from payments.models import StripeCard
from django.contrib.auth.decorators import login_required


@login_required
def add_card(request):
    return render(request, 'payments/add_card.html', {})


class StripeCardListView(LoginRequiredMixin, ListView):
    model = StripeCard
    template_name = 'payments/cards.html'


