from django.urls import path

from .views import CreateShortLink, RedirectShortLinkView

app_name = 'api'

urlpatterns = [
    path('tokens/', CreateShortLink.as_view()),
    path('<str:token>/', RedirectShortLinkView.as_view())
]
