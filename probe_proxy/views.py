from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the probe_proxy index.")


def breached(request, email):
    target_url = 'https://haveibeenpwned.com/api/v3/breachedaccount/' + email
    headers = {'hibp-api-key': '77acd09d8685422ba1df125572c4f698'}
    response = requests.request(
        method='GET',
        url=target_url,
        headers=headers,
        data=request.body,
    )
    if not response.text:
        return JsonResponse(data=[], status=200, safe=False)

    return JsonResponse(data=response.json(), status=response.status_code, safe=False)
