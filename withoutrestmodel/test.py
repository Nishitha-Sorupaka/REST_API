import requests,json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    resp = requests.get(BASE_URL + END_POINT, data = json.dumps(data))
    print('Status Code : {}'.format(resp.status_code))
    print(resp.json())

#id = input('Enter Some Id: ')
get_resource()

def update_resource(id=None):
    new_emp = {
        'id': id,
        'esal': 70000,
        'eaddr': 'Delhi'
    }
    resp = requests.put(BASE_URL + END_POINT,data=json.dumps(new_emp))
    print('Status Code : {}'.format(resp.status_code))
    print(resp.json())
#update_resource(8)

def delete_resource(id=None):
    data = {'id': id}
    resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(data))
    print('Status Code : {}'.format(resp.status_code))
    print(resp.json())

#delete_resource()

def create_resource():
    new_emp = {
        'eno': 107,
        'ename': 'Yash',
        'esal': 5001,
        'eaddr': 'Armor'
    }
    resp = requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
    print('Status Code : {}'.format(resp.status_code))
    print(resp.json())
#create_resource()

'''
def get_resource(id):
    resp = requests.get(BASE_URL + END_POINT+id)
    print('Status Code : {}'.format(resp.status_code))
    #if resp.status_code in range(200, 300):
    if resp.status_code == requests.codes.ok:
        print(resp.json())
    else:
        print('Something went wrong.....')



def get_all():
    resp = requests.get(BASE_URL + END_POINT)
    print(resp.status_code)
    print(resp.json())
get_all()

'''