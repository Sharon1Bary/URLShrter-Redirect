# URL shortener redirects Service Introduction:

URL shortener redirects is a redirect engine.

## Installation
* Download the project - https://github.com/Sharon1Bary/URLShrter-Redirect
* Create Virtual Environment
```bash
py -m venv myworld
```
* Loging to the Virtual Environment
```bash
 myworld\Scripts\activate.bat
```
* Install requirements.txt file.
* Run server
```bash
py manage.py runserver
```
* Create a new Short-URL (The Short-URL will return - ex - {"return": "http://127.0.0.1:8000/s/JAJ8HBm"})

```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/create/ -d "{\"url\":\"https://ravkavonline.co.il\"}"   
```

* Redirect from the Short-URL to the Original URL by linking to http://127.0.0.1:8000/s/JAJ8HBm (in your case will be difference 7 last digits).


## Django Admin to manag the data 
* create a super-user to http://127.0.0.1:8000/admin/
```bash
py manage.py createsuperuser
```
