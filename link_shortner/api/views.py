from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView
from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin

from .serializers import ShortLinkSerializer
from .models import ShortLink

class CreateShortLink(CreateAPIView):
    serializer_class = ShortLinkSerializer
 
    
class RedirectShortLinkView(RedirectView):
   
   def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
       link = get_object_or_404(ShortLink, token=kwargs['token'])
       return link.long_url