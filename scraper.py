import httpx

URL = 'https://portal-ohmedina.tylertech.cloud/Portal/'

r = httpx.get(URL)

statusCode = r.status_code
headers = r.headers
startPage = r.text

print(startPage)