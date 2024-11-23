from django.contrib import admin
from django.utils.html import format_html

from drones.models import Drone, Competition, DroneCategory, Pilot


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "drone_category",
        "manufacturing_date",
        "has_it_competed",
        "is_published",
        "display_picture",
        "owner",
    )
    list_editable = ("is_published", "drone_category")
    search_fields = ("name", "drone_category__name", "owner__username")
    list_filter = ("drone_category", "has_it_competed", "is_published", "owner")
    # readonly_fields = ("owner",)
    save_on_top = True

    def display_picture(self, obj):
        if obj.picture:
            return format_html(
                '<img src="{}" width="50" height="50" />', obj.picture.url
            )
        return "Sem imagem"

    display_picture.short_description = "Imagem"


@admin.register(DroneCategory)
class DroneCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    pass


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("pilot", "drone", "distance_in_feet", "distance_achievement_date")
    search_fields = ("pilot__name", "drone__name")
    list_filter = ("distance_achievement_date", "drone__drone_category")
    date_hierarchy = "distance_achievement_date"
    save_on_top = True

    fieldsets = (
        (
            "Selecionar Piloto e Drone",
            {
                "fields": (
                    "pilot",
                    "drone",
                )
            },
        ),
        (
            "Adicionar Detalhes da Competição",
            {
                "fields": (
                    "distance_in_feet",
                    "distance_achievement_date",
                )
            },
        ),
    )
