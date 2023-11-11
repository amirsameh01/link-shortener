import string
from django.views import View
from django.http import JsonResponse
from urlgenerator.models import Urls
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from urlgenerator.models import Urls
from .serializers import UrlsSerializer
import random


class LinkCreator(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = Urls.objects.all()

        serializer = UrlsSerializer(queryset, many=True)
        response = JsonResponse(serializer.data, safe=False)

        return response

    def post(self, request):

        url = request.POST.get('url')
        code = request.POST.get('code')
        shortcodes = Urls.objects.values_list("url_shortened")

        if code:
            if code not in shortcodes:
                slug = code

        else:
            characters = string.ascii_letters + string.digits
            slug = ''.join(random.choice(characters) for _ in range(10))

        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        
        return JsonResponse({'original': url, 'short': slug}) 
   