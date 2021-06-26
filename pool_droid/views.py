from django.http import HttpResponse
from django.views import View

from pool_droid.utils import get_cabinet_temp


class HomeView(View):
    def get(self, request):
        temp_c, temp_f = get_cabinet_temp()
        return HttpResponse(f"Cabinet Temp: {temp_c} °C, {temp_f} °F")
