from django.contrib import admin, messages
from django.utils.translation import ngettext

from pool_droid.models import Relay, OneWireTempSensor


@admin.register(Relay)
class RelayAdmin(admin.ModelAdmin):
    list_display = ["name", "gpio_bcm", "initial_state", "get_state"]
    actions = ["enable_relay", "disable_relay"]

    @admin.action
    def enable_relay(self, request, relays):
        for relay in relays:
            relay.set_state(True)
        self.message_user(request, ngettext(
            '%d relay was successfully enabled.',
            '%d relays were successfully enabled.',
            relays.count(),
        ) % relays.count(), messages.SUCCESS)

    @admin.action
    def disable_relay(self, request, relays):
        for relay in relays:
            relay.set_state(False)
        self.message_user(request, ngettext(
            '%d relay was successfully disabled.',
            '%d relays were successfully disabled.',
            relays.count(),
        ) % relays.count(), messages.SUCCESS)


@admin.register(OneWireTempSensor)
class OneWireTempSensorAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "get_temps"]
