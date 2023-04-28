import requests


class BigSearch(object):
    def __init__(self):
        self.server = "https://geocode-maps.yandex.ru/1.x/"
        self.apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

    def getting_ad(self, address: str):
        self.geocode = address
        self.kind = ""
        self.get_request()

    def putting_cor(self, ll: tuple, kind=""):
        self.geocode = ",".join(map(str, ll))
        self.kind = kind
        self.get_request()

    def getting_cor(self, index: int):
        feature_member = self.json_resp["response"]["GeoObjectCollection"]["featureMember"][index]
        ll_string = feature_member["GeoObject"]["Point"]["pos"]
        return tuple(map(float, ll_string.split()))

    def getting_2(self, index: int):
        feature_member = self.json_resp["response"]["GeoObjectCollection"]["featureMember"][index]
        return feature_member["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]

    def get_request(self):
        pars = {
            "apikey": self.apikey,
            "geocode": self.geocode,
            "format": "json"
        }
        if self.kind:
            pars["kind"] = self.kind
        response = requests.get(self.server, pars)
        if not response:
            print(f"Error: {response.status_code} ({response.reason})")
        self.json_resp = response.json()


search = BigSearch()
search.getting_ad(input())
coors = search.getting_cor(0)
search.putting_cor(coors, "district")
try:
    print((search.getting_2(1)).split(',')[2].strip())
except:
    print("ERROR")
