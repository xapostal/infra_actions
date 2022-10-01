"""Views infra_app."""

from django.http import HttpResponse


def index(request):
    """ss."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """sfs."""
    return HttpResponse('А это вторая страница!')
