import requests,json
BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'
def get_resource(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    resp = requests.get(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#get_resource()

def create_resource():
    data = {
        'eno': 102,
        'ename': 'Nishu',
        'esal': 50000,
        'eaddr': 'Vijayawada'
    }
    resp = requests.post(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#create_resource()

def update_resource(id=None):
    data = {
        'id': id,
        #'ename': 'sunny123',
        'esal': 50001,
        'eaddr': 'Mumbai'
    }
    resp = requests.put(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

update_resource(6)

def delete_resource(id=None):
    data = {
        'id': id,
    }
    resp = requests.delete(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#delete_resource(3)