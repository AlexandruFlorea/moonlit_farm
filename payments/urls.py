from django.urls import path
from payments.views import add_card, StripeCardListView


app_name = 'payments'

urlpatterns = [
    path('add_card/', add_card, name='add_card'),
    path('cards/', StripeCardListView.as_view(), name='cards'),

]
