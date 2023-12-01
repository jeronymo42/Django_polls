from django.urls import path
from main.views import IndexView, DetailsView, ResultsView, vote

app_name = "polls"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailsView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]
