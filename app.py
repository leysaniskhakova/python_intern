import requests

from requests.exceptions import ConnectionError

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
def is_alive_host(hostname: str):
    try:
        response = requests.get('http://' + hostname)
    except ConnectionError as e:
        return {'status': 'down'}

    code = response.status_code
    if 100 <= code < 400:
        return {'status': 'up'}
    return {'status': 'down'}
