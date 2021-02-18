import requests
import json
import jsonpath
import random

baseUrl = "https://reqres.in/"

def test_successful_registration() :
    path = "api/register"
    response = requests.post(url=baseUrl+path,json=json.loads('{"email": "eve.holt@reqres.in","password": "'+randomDigits(5)+'"}'))
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert type(jsonpath.jsonpath(responseJson,'$.token')[0]) == str


def test_unsuccessful_registration() :
    path = "api/register"
    response = requests.post(url=baseUrl+path,json=json.loads('{"email": "testemail@pytest.com"}'))
    responseJson = json.loads(response.text)
    assert response.status_code == 400
    assert jsonpath.jsonpath(responseJson,'$.error')[0] == 'Missing password'


def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return str(random.randint(lower, upper))