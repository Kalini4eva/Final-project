import configuration
import data
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


response = post_new_order(data.body)


print(response.status_code)
print(response.json())


def get_track_order():
    track_order = post_new_order(data.body).json()["track"]
    return track_order


print(response.json())


def get_order_track(order):
    track = get_track_order()
    payload = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK, params=payload)


response = get_order_track(data.order_body)

print(response.status_code)
print(response.json())

