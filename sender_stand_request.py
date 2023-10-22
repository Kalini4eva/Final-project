import configuration
import data
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


def get_track_order(track):
    track_order = post_new_order(data.body).json()["track"]
    return track_order


def get_order_track(track):
    track = get_track_order(track)
    payload = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK, params=payload)
