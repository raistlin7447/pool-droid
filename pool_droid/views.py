from django.views.generic import TemplateView

from pool_droid.models import Relay, OneWireTempSensor, PentairPump


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors'] = OneWireTempSensor.objects.all()
        context['relays'] = Relay.objects.all()
        context['pumps'] = PentairPump.objects.all()
        return context


class TestHomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors'] = [{"name": "Cabinet", "get_temp_f": "98.6"}]
        context['relays'] = [
            {"name": "Booster Pump", "get_state": True},
            {"name": "Relay 2", "get_state": False},
            {"name": "Relay 3", "get_state": False},
            {"name": "Relay 4", "get_state": False},
        ]
        context['pumps'] = [{'name': 'Main Pump', 'get_status': PentairPump.format_status({'run': 4, 'mode': 0, 'watts': 0, 'rpm': 0, 'timer': [0, 0], 'time': [11, 13]})}]
        return context
