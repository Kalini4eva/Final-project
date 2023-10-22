#Калиничева Алена, 9-поток, финальный проект. Инженер по тестированию плюс.

import sender_stand_request


def test_order():
    test_order.response = sender_stand_request.get_order_track('order')

    assert test_order.response.status_code == 200
