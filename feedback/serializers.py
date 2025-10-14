from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    from_user = serializers.ReadOnlyField(source="from_user.id")
    from_user_email = serializers.ReadOnlyField(source="from_user.email")
    to_user_email = serializers.ReadOnlyField(source="to_user.email")

    class Meta:
        model = Feedback
        fields = ["id", "from_user", "from_user_email", "to_user", "to_user_email", "comment", "created_at"]
        read_only_fields = ["from_user", "from_user_email", "to_user_email", "created_at"]
