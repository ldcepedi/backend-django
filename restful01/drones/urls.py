from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("drone-categories", views.DroneCategoryViewSet)

urlpatterns = [
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path(
        "competitions/",
        views.CompetitionList.as_view(),
        name=views.CompetitionList.name,
    ),
    path(
        "competitions/<int:pk>/",
        views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name,
    ),
    path("", include(router.urls)),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
