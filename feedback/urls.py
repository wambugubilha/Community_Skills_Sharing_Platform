from django.urls import path
from .views import FeedbackListCreateView, FeedbackDetailView

urlpatterns = [
    path("", FeedbackListCreateView.as_view(), name="feedback-list-create"),
    path("<int:pk>/", FeedbackDetailView.as_view(), name="feedback-detail"),
]
