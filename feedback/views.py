from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class FeedbackListCreateView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # allow user to see feedback they received or gave
        user = self.request.user
        q = Feedback.objects.filter(to_user=user) | Feedback.objects.filter(from_user=user)
        return q.distinct()

    def perform_create(self, serializer):
        # ensure to_user exists and not same as from_user (optional)
        to_user_id = self.request.data.get("to_user")
        to_user = get_object_or_404(User, id=to_user_id)
        if to_user == self.request.user:
            raise serializers.ValidationError("Cannot leave feedback for yourself.")
        serializer.save(from_user=self.request.user, to_user=to_user)


class FeedbackDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # user can only view/delete feedback they gave or received
        user = self.request.user
        return Feedback.objects.filter(to_user=user) | Feedback.objects.filter(from_user=user)
