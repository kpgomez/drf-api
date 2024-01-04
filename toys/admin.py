from django.contrib import admin
from .models import Toy


class ToyAdmin(admin.ModelAdmin):
    list_display = (
        "purchaser",
        "title",
        "description",
        "created_at",
        "updated_at"
    )


# Register your models here.
admin.site.register(Toy, ToyAdmin)
