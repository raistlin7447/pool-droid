from django.contrib import admin

from pool_droid.models import Relay


@admin.register(Relay)
class RelayAdmin(admin.ModelAdmin):
    list_display = ["name", "gpio_bcm", "initial_state", "get_state"]
