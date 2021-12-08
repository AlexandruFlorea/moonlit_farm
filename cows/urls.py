from django.urls import path
from cows.views import show_all_cows, cow_details


app_name = 'cows'

urlpatterns = [
    path('', show_all_cows, name='all'),
    path('<cow_id>/', cow_details, name='details'),

]
