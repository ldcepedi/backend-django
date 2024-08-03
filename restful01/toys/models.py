from django.db import models


class Toy(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, default="")
    description = models.CharField(max_length=250, blank=False, default="")
    release_date = models.DateTimeField()
    toy_category = models.CharField(max_length=200, default="")
    was_included_in_home = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
