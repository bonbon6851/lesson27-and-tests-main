# Задание 1. tech support.py

from django.http import JsonResponse
from .models import Statistic


def statistics(request):
    # TODO напишите view-функцию которая возвращает всю статистику
    #  обращений в тех-поддержку (задание tech_support)
    if request.method == "GET":
        statistics_data = Statistic.objects.all()

        response = []
        for statistic in statistics_data:
            response.append({
                "store": statistic.store,
                "author": statistic.author,
                "status": statistic.status,
                "day": statistic.day,
                "reason": statistic.reason,
                "timestamp": statistic.timestamp
            })
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
