from django.shortcuts import render
from django.http import JsonResponse
from .models import SampleModel

# Create your views here.
def health(request):
    return JsonResponse({'status': 'ok'})

def list_samples(request):
    data = list(SampleModel.objects.all().values("id", "name", "version", "description"))
    return JsonResponse(data, safe=False)
