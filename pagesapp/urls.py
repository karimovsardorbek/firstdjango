from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, HistoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('history/', HistoryPageView.as_view(), name='history'),
]