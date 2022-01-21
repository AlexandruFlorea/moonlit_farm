from django.urls import path
from activities.views import ActivityListView, ActivityDetailView


app_name = 'activities'

urlpatterns = [
    # path('', show_all_activities, name='all'),
    # path('<activity_id>/', activity_details, name='details'),
    path('', ActivityListView.as_view(), name='all'),
    path('<int:pk>/', ActivityDetailView.as_view(), name='details'),

]
