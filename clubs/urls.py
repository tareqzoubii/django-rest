from django.urls import path
from .views import ClubsListView,ClubsDetailView
urlpatterns = [
   path('', ClubsListView.as_view(), name='clubs_list'),
   path('<int:pk>', ClubsDetailView.as_view(),name='clubs_detail')
]