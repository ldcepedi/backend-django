from django_filters import rest_framework as filters
from drones.models import Competition


class CompetitionFilter(filters.FilterSet):
    from_achievement_date = filters.DateFilter(
        field_name="distance_achievement_date", lookup_expr="gte"
    )
    to_achievement_date = filters.DateFilter(
        field_name="distance_achievement_date", lookup_expr="lte"
    )
    min_distance_in_feet = filters.NumberFilter(
        field_name="distance_in_feet", lookup_expr="gte"
    )
    max_distance_in_feet = filters.NumberFilter(
        field_name="distance_in_feet", lookup_expr="lte"
    )
    drone_name = filters.AllValuesFilter(field_name="drone__name")
    pilot_name = filters.AllValuesFilter(field_name="pilot__name")

    class Meta:
        model = Competition
        fields = (
            "distance_in_feet",
            "from_achievement_date",
            "to_achievement_date",
            "min_distance_in_feet",
            "max_distance_in_feet",
            # drone__name vai ser acessado como drone_name
            "drone_name",
            # pilot__name vai ser acessado como pilot_name
            "pilot_name",
        )
