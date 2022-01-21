from django.shortcuts import render, redirect, get_object_or_404
from cows.models import Cow
from django.views.generic import ListView, DetailView


class CowListView(ListView):
    model = Cow
    template_name = 'cows/cow_list.html'


class CowDetailView(DetailView):
    model = Cow
    template_name = 'cows/cow_detail.html'


# def show_all_cows(request):
#     cows = Cow.objects.all()
#
#     return render(request, 'cows/cows.html', {
#         'cows': cows
#     })
#
#
# def cow_details(request, cow_id):
#     cow = get_object_or_404(Cow, pk=cow_id)
#
#     return render(request, 'cows/details.html', {
#         'cow': cow
#     })
