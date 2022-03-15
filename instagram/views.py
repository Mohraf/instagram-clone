from django.views import generic
# from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.template import RequestContext

from post.models import Post
from post.helpers import get_posts


class HomePageView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return get_posts(self.request.user, wall=True)


def handler404(request):
    response = TemplateResponse(
        '404.html', {},
        context_instance=RequestContext(request)
    )
    response.status_code = 404
    return response