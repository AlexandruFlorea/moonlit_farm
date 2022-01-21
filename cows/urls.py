from django.urls import path
from cows.views import CowListView, CowDetailView


app_name = 'cows'

urlpatterns = [
    # path('', show_all_cows, name='all'),
    # path('<cow_id>/', cow_details, name='details'),
    path('', CowListView.as_view(), name='all'),
    path('<int:pk>/', CowDetailView.as_view(), name='details'),

]
