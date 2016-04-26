from django.shortcuts import get_object_or_404, render

from .models import Page


def show_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page.html', {'page': page})
