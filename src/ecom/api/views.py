from django.http import JsonResponse, HttpResponse


def home(request):
    return JsonResponse({'name': 'sanket'})