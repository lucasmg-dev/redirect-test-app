from django.http import JsonResponse
from .models import Redirect
from .exceptions import RedirectKeyNotExist


def get_redirect_key(request):
    key = request.GET.get('key')
    try:
        redirect = Redirect.get_redirect(key)
        return JsonResponse(redirect)
    except RedirectKeyNotExist as e:
        return JsonResponse({
            'status': 'error',
            'description': str(e)
        })
