from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup 
import requests

from myapp.models import Link


def scrape(request):
    site = request.POST.get('site','')
    if request.method == 'POST' and site != '':
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
       
    return render(request,'myapp/result.html',{'data':data}) 


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')