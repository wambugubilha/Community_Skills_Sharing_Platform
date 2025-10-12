from django.db import models
from django.conf import settings

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("Tech", "Tech"),
        ("Cooking", "Cooking"),
        ("Art", "Art"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.email}"
