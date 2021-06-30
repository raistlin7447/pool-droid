from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from pool_droid.models import Relay, OneWireTempSensor, PentairPump
from pool_droid.utils import get_pump_speed


class HomeView(View):
    def get(self, request):
        temp_str = ""
        for sensor in OneWireTempSensor.objects.all():
            temp_str += f"{sensor.name}: {sensor.get_temp_f()} °F, "

        relay_str = ""
        for relay in Relay.objects.all():
            relay_str += f"{relay.name}: {relay.get_state()}, "

        pump_str = ""
        for pump in PentairPump.objects.all():
            relay_str += f"{pump.name}: {pump.get_speed()}, "

        return HttpResponse(f"{temp_str}{relay_str}{pump_str}")


class TestHomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors'] = OneWireTempSensor.objects.all()
        context['relays'] = Relay.objects.all()
        context['pumps'] = PentairPump.objects.all()
        return context

class Test2HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors'] = [{"name": "Cabinet", "get_temp_f": "98.6 F"}]
        context['relays'] = [
            {"name": "Booster Pump", "get_state": True},
            {"name": "Relay 2", "get_state": False},
            {"name": "Relay 3", "get_state": False},
            {"name": "Relay 4", "get_state": False},
        ]
        context['pumps'] = [{"name": "Main Pump", "get_speed": "1750"}]
        return context
