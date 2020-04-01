import requests
import pytest

def get_all_people_name():
    return "https://aa6d3f9a-f479-4dfd-b4e7-566f2af94071.mock.pstmn.io/names"

def get_person_info_by_name(name):
    return "https://aa6d3f9a-f479-4dfd-b4e7-566f2af94071.mock.pstmn.io/person-info?name="+name


response_names = requests.get(get_all_people_name())
print(response_names.json())

response_info = requests.get(get_person_info_by_name("Marty"))
print(response_info.json())


