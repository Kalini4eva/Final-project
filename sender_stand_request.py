import configuration
import data
import requests


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.body)


def get_order_by_track_number(parametr):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK, params=parametr)
