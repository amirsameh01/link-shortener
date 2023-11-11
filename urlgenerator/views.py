from django.shortcuts import get_object_or_404, render, redirect
from .models import Urls
from django.contrib import messages
from django.views import View
from .forms import InputForm
import requests


def home(request):
    form = InputForm()

    if request.user.is_authenticated:
        urls = Urls.objects.filter(user=request.user)
        context = {
            'form': form,
            'urls': urls,
        }
    else:
        context = {
            'form': form,
        }
    return render(request, "index.html", context)


class CreateShortUrl(View):

    def post(self, request):
        form = InputForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            custom_url = form.cleaned_data['custom_code']
            API_URL = 'http://127.0.0.1:8000/generate/'
            data = {"url": url, "code": custom_url}
            
            response = requests.post(API_URL, data=data)
            
            short_url = response.json()['short'] 
            original_url = response.json()['original']

            new_url = Urls(url_original=original_url, url_shortened=short_url, user=request.user)
            new_url.save()

            
        return redirect("home")



def Redirecting(request, shortcode):
    link = get_object_or_404(Urls, url_shortened=shortcode)
    link.clicks += 1
    link.save()
    return redirect(link.url_original)
