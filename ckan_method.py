import requests
import json


def get_ckan_data():
    url = "http://demo.ckan.org/api/3/action/package_list"
    params = {"q": 'tags: "data"'}
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == "__main__":
    data = get_ckan_data()
    print(data)
