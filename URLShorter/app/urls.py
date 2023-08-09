from django.urls import path, re_path
from .views import URLShorter
from .views import URL

"""
    used regex to catch all the short-url, by the following format - http://127.0.0.1:8000/s/iMxeFRW
"""
all_url_data = URL.objects.all()

urlpatterns = [
    re_path(r"(s/.*?)$", URLShorter.redirect_url),
    path('create/', URLShorter.as_view()),
]
