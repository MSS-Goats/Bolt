from django.shortcuts import render

from analysis.models import NavItem


def index(request):
    nav_item_list = NavItem.objects.all().order_by('order')
    context = {'nav_item_list': nav_item_list}
    return render(request, 'analysis/index.html', context)
