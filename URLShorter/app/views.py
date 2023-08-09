from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

import json
import bcrypt
from .models import URL


@method_decorator(csrf_exempt, name='dispatch')
class URLShorter(View):

    def post(self, request):
        """
        post methode is gets the create request and generate a new unique short-url by encrypting the url using
        bcrypt (it's use salt) hash, store the new short-url in the DB and initialize the hit-counter for each short-url.
        every url can have multiple short-url (each shor-url manage separately).
        """
        try:
            data = json.loads(request.body.decode("utf-8"))
            url_path = data.get('url')
            short_url = 'http://127.0.0.1:8000/s/' + self.encrypt(url_path)

            if self.is_new_url(url_path, short_url):
                URL.objects.create(**{
                    'url': url_path,
                    'url_data': {"short_urls": {short_url: 0}}
                })
            data = {"return": f"{short_url}"}

            return JsonResponse(data, status=201)
        except ValueError as e:
            print(e.__context__)

    @staticmethod
    def encrypt(url: str) -> str:
        """
        encryption the url using bcrypt (salt) hash and generate a unique url by tacking the last 7 digits.
        """
        hashed = bcrypt.hashpw(url.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode("utf-8")[-7:]

    @staticmethod
    def is_new_url(url: str, short_url: str) -> bool:
        """
        checking if the url provided is already in the system,
        if yes it's snapping the short-url to the url by updating the db.
        """
        all_url_data = URL.objects.all()

        for url_row in all_url_data:
            if url_row.url == url:
                url_row.url_data["short_urls"][short_url] = 0
                url_row.save()
                return False
        return True

    @staticmethod
    def redirect_url(request, x):
        """
        get the urls data from the db and based on the short-url it increase the hint-counter by 1
        and redirect the request to the original url.
        """
        try:
            all_url_data = URL.objects.all()

            for url_row in all_url_data:
                url_pers = [{'url': url_row.url, 'short_url': short_url}
                            for short_url in list(url_row.url_data["short_urls"].keys())
                            if short_url[-7:] == request.path[-7:]]
                if url_pers:
                    url_row.url_data["short_urls"][url_pers[0]['short_url']] += 1
                    url_row.save()
                    return redirect(url_pers[0]['url'])
        except ValueError as e:
            print(e.__context__)
