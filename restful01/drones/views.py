from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DroneCategory, Drone, Pilot, Competition
from drones.serializers import (
    DroneCategorySerializer,
    DroneSerializer,
    PilotSerializer,
    PilotCompetitionSerializer,
)
from rest_framework import viewsets
from drones.filters import CompetitionFilter
from rest_framework import permissions
from drones import custom_permissions
from rest_framework.authentication import TokenAuthentication


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "drone-categories": reverse("dronecategory-list", request=request),
                "drones": reverse(DroneList.name, request=request),
                "pilots": reverse(PilotList.name, request=request),
                "competitions": reverse(CompetitionList.name, request=request),
            }
        )


class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    search_fields = ("^name",)
    ordering_fields = ("name",)


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"
    filterset_fields = (
        "drone_category",
        "has_it_competed",
    )
    search_fields = ("^name",)
    ordering_fields = (
        "name",
        "manufacturing_date",
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"
    filterset_fields = (
        "gender",
        "races_count",
    )
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"
    filterset_class = CompetitionFilter
    ordering_fields = (
        "distance_in_feet",
        "distance_achievement_date",
    )


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-detail"
