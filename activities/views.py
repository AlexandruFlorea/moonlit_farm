from django.shortcuts import render, redirect, get_object_or_404
from activities.models import Activity


def show_all_activities(request):
    return render(request, 'activities/activities.html', {})


def activity_details(request, activity_id):
    activity = get_object_or_404(Activity, activity_id)

    return render(request, 'activities/details.html', {
        'activity': activity
    })
