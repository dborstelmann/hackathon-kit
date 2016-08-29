from django.template.response import TemplateResponse
from django.contrib.auth.models import User


def base_view(request):
    if not request.user.is_authenticated():
        return TemplateResponse(request, 'base/404.html', {})

    return TemplateResponse(request, 'hello.html', {})
