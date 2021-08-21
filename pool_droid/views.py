import json

from django.http import JsonResponse
from django.views import View
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
            {"id": 1, "name": "Booster Pump", "get_state": True},
            {"id": 2, "name": "Relay 2", "get_state": False},
            {"id": 3, "name": "Relay 3", "get_state": False},
            {"id": 4, "name": "Relay 4", "get_state": False},
        ]
        # status = {'run': 4, 'mode': 0, 'watts': 0, 'rpm': 0, 'timer': [0, 0], 'time': [13, 13]} #off
        status = {'run': 10, 'mode': 1, 'watts': 334, 'rpm': 1750, 'timer': [24, 1], 'time': [18, 59]} # running
        context['pumps'] = [{'name': 'Main Pump', 'get_status': PentairPump.format_status(status)}]
        return context


class PumpModeAjax(View):
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            pump_mode_json = json.loads(self.request.body)
            pump_mode = pump_mode_json["pump-mode"]
            print(self.request.body)
            pump = PentairPump.objects.get()
            if pump_mode == "qc":
                pump.start_quick_clean()
            else:
                pump.set_speed(int(pump_mode))
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=400)
