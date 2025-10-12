from django.urls import path
from .views import SkillListCreateView, SkillDetailView

urlpatterns = [
    path("", SkillListCreateView.as_view(), name="skills-list"),
    path("<int:pk>/", SkillDetailView.as_view(), name="skills-detail"),
]
