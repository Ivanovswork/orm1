from django.shortcuts import render, redirect
from phones.models import Phone
from operator import itemgetter


def index(request):
    return redirect('catalog')


def show_catalog(request):
    srt = request.GET.get('sort', "name")
    template = 'catalog.html'
    ph = Phone.objects.all()
    if srt == "name":
        phones = sorted(list(ph), key=lambda e: e.name)
    elif srt == "min_price":
        phones = sorted(list(ph), key=lambda e: int(e.price))
    elif srt == "max_price":
        phones = sorted(list(ph), key=lambda e: int(e.price), reverse=True)
    context = \
        {
            'phones': phones,
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.filter(slug=slug)
    # print(p[0].name)
    context = \
        {
            'phone': p[0],
        }
    return render(request, template, context)
