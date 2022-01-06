from django.shortcuts import render, redirect, get_object_or_404
from activities.models import Activity


def show_all_activities(request):
    activities = Activity.objects.all()

    return render(request, 'activities/activities.html', {
        'activities': activities,
    })


def activity_details(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    return render(request, 'activities/details.html', {
        'activity': activity
    })
