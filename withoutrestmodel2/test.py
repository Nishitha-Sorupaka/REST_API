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
get_resource()

def create_resource():
    new_std = {
        'name':'Naresh',
        'rollno': 105,
        'marks': 67,
        'gf': 'Priya',
        'bf': 'Chanti'
    }
    resp = requests.post(BASE_URL + END_POINT , data = json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())
#create_resource()

def update_resource(id=None):
    data = {
        'id':id,
        'marks': 66,
        'gf': 'Shoba',
        'bf': 'Remo'
    }
    resp = requests.put(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#update_resource()

def delete_resource(id=None):
    data = {'id': id}
    resp = requests.delete(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#delete_resource(5)