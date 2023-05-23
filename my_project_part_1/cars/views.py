from django.http import JsonResponse

from cars.models import Car


def get_car(request, pk):
    cars = Car.objects.all()

    for car in cars:
        if car.pk == int(pk):
            car_pk = {
                'slug':  car.slug,
                'name':  car.name,
                'brand': car.brand,
                'address':   car.address,
                'description':   car.description,
                'status':    car.status,
                'created':   car.created
            }
            return JsonResponse(car_pk, safe=False, json_dumps_params={"ensure_ascii": False})


def search(request):
    if request.method == "GET":
        car_list = Car.objects.all()

        brand = request.GET.get("brand", None)

        if brand:
            cars = car_list.filter(brand=brand)

            result = []
            for car in cars:
                result.append({
                    "id": car.id,
                    "name": car.name,
                    "brand": car.brand,
                    "status": car.status
                })

            return JsonResponse(result, safe=False)
