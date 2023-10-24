#Калиничева Алена, 9-поток, финальный проект. Инженер по тестированию плюс.

import data
import sender_stand_request


def create_order():
    track = sender_stand_request.post_new_order()
    return str(track.json()["track"])


def test_get_order_by_track_success():
    track = create_order()
    current_params = data.track.copy()
    current_params["t"] = track
    response = sender_stand_request.get_order_by_track_number(current_params)
    assert response.status_code == 200

