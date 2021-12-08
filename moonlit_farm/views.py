from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html', {})


def about_page(request):
    return render(request, 'about_us.html', {})
