import requests
import json
import jsonpath

baseUrl = "https://reqres.in/"

def test_fetch_user() :
    path = "api/users/2"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2


def test_create_delete_user() :
    path = "api/users"
    response = requests.post(url=baseUrl+path,json=json.loads('{"name": "morpheus","job": "leader"}'))
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    assert jsonpath.jsonpath(responseJson,'$.name')[0] == 'morpheus'
    id = jsonpath.jsonpath(responseJson,'$.id')[0]
    response = requests.delete(url=baseUrl+path+'/'+id)
    assert response.status_code == 204