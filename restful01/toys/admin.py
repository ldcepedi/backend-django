from django.contrib import admin

from toys.models import Toy


class ToyAdmin(admin.ModelAdmin):
    list_display = ["name", "toy_category"]
    search_fields = ["name", "toy_category"]
    list_filter = ("toy_category", "release_date", "was_included_in_home")


admin.site.register(Toy, ToyAdmin)
# admin.site.register(Toy)
