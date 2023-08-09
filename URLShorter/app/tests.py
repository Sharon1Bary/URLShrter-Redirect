import requests
import json
import webbrowser


def test_create_and_redirect():

    """
    The test is creates a new url_row in the DB based on the url provided.
        A post request.
    Then it redirect from the short_url to the provided URL.
    """

    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"url": "https://ravkavonline.co.il"}'
    response = requests.post('http://localhost:8000/create/', headers=headers, data=data)

    assert response.status_code == 201

    redirect_response = webbrowser.open(json.loads(response.content.decode("utf-8"))['return'])

    assert redirect_response is True
