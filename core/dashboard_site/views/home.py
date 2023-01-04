from django.shortcuts import render


def index_page(request):
    template_name = "dashboard_site/index.html"

    return render(request, template_name, {})
