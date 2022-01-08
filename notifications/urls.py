from django.urls import path
from notifications.views import show_notifications, mark_as_seen, mark_unseen


app_name = 'notifications'

urlpatterns = [
    path('', show_notifications, name='view_all'),
    path('<int:id>/mark_as_seen', mark_as_seen, name='mark_as_seen'),
    path('<int:id>/mark_unseen', mark_unseen, name='mark_unseen'),

]
