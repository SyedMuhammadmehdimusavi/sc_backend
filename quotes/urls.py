from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import path
from quotes.views import QuoteList , QuoteDetail
urlpatterns = [
    path('quotes/',QuoteList.as_view()),
    path('quotes/<int:pk>',QuoteDetail.as_view())
]
