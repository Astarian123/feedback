from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),         #Change for class reference
    path('thank-you/', views.ThankYouView.as_view()),
    path('list/', views.ReviewsListView.as_view()),
    path('<int:pk>/', views.DeailView.as_view())
]
