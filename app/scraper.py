from app import htmlParser
import httpx

parser = htmlParser.MyHTMLParser()

def OHIO_MEDINA():
    URL = 'https://portal-ohmedina.tylertech.cloud/Portal/'
    r = httpx.get(URL)

    statusCode = r.status_code
    headers = r.headers
    startPage = r.text
    startPageParser = htmlParser.MyHTMLParser()
    return startPage, headers, statusCode

def LANCASTER():
    URL = 'https://it.co.lancaster.pa.us/SPS/Public/'
    r = httpx.post(URL)
    statusCode = r.status_code
    headers = r.headers
    startPage = r.text
    startPageParser = htmlParser.MyHTMLParser()
    return startPage, headers, statusCode


responseLancaster = LANCASTER()
responseOhio = OHIO_MEDINA()