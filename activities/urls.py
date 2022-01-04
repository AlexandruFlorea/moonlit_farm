from django.urls import path
from activities.views import show_all_activities, activity_details


app_name = 'activities'

urlpatterns = [
    path('', show_all_activities, name='all'),
    path('<activity_id>/', activity_details, name='details'),

]
