from django.http import JsonResponse

from courses.models import Course


def courses(request):
    courses_list = Course.objects.all()
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


def new_courses(request):
    if request.method == "GET":
        courses_list = Course.objects.all()
        result = []
        for course in courses_list:
            if course.status == "new":
                result.append({
                    "id": course.id,
                    "slug": course.slug,
                    "author": course.author,
                    "description": course.description,
                    "start_day": course.start_day,
                    "status": course.status,
                    "created": course.created,
                })
        return JsonResponse(result, safe=False, json_dumps_params={"ensure_ascii": False})


def get_course(request, slug):
    if request.method == "GET":
        courses_list = Course.objects.all()
        for course in courses_list:
            if course.slug == slug:
                result = {
                    "id": course.id,
                    "slug": course.slug,
                    "author": course.author,
                    "description": course.description,
                    "start_day": course.start_day,
                    "status": course.status,
                    "created": course.created,
                }
        return JsonResponse(result, safe=False, json_dumps_params={"ensure_ascii": False})


def search(request):
    courses_list = Course.objects.all()
    author = request.GET.get("author", None)

    if author is not None:
        courses_list = courses_list.filter(author=author)

        result = []

        for course in courses_list:
            result.append({
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            })
        return JsonResponse(result, safe=False, json_dumps_params={"ensure_ascii": False})
