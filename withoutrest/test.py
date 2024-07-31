import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsoncbv/'
response = requests.get(BASE_URL+ENDPOINT)
#print(response.json())
#print(type(response.json))
#print(type(response))
data = response.json()
print(data)
'''
print("Data From django application:")
print('-'*30)
print("Employee Number : {}".format(data['eno']))
print("Employee Name : {}".format(data['ename']))
print("Employee Salary : {}".format(data['esal']))
print("Employee Address : {}".format(data['eaddr']))
'''