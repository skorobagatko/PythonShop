from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string


def home(request):
    categories = Category.objects.all()
    # return HttpResponse(render_to_string('index.html'), context)
    return render(request, 'home.html', locals())


def item(request, alias):
    try:
        tovar = Item.objects.get(alias=alias)
    except:
        raise Http404('Объект не найден')
    return render(request, 'item.html', locals())


def category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        tovary = Item.objects.filter(category=category)
    except:
        raise Http404('Объект не найден')
    return render(request, 'index.html', locals())


def order(request):
    return render(request, 'order.html', locals())