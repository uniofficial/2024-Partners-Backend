from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import ShortLink
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_short_link(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            original_url = data['original_url']

            # URL이 이미 존재하는지 확인
            try:
                short_link = ShortLink.objects.get(original_url=original_url)
            except ShortLink.DoesNotExist:
                short_link = ShortLink(original_url=original_url)
                short_link.save()

            response_data = {
                'original_url': short_link.original_url,
                'short_url': short_link.short_url,
                'hash_value': short_link.hash_value,
                'created_at': short_link.created_at
            }
            return JsonResponse(response_data)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def redirect_short_link(request, hash_value):
    short_link = get_object_or_404(ShortLink, hash_value=hash_value)
    return redirect(short_link.original_url)

def home(request):
    return render(request, 'urlshortenerapp/home.html')
