"""Tests for device type validation on create and update endpoints."""

from app.schemas.device import DeviceType

VALID_TYPES = [device_type.value for device_type in DeviceType]


def test_create_accepts_all_valid_device_types(client):
    """Every supported device type must be accepted on create (200)."""
    for device_type in VALID_TYPES:
        response = client.post(
            "/devices/",
            json={
                "name": f"Test {device_type}",
                "type": device_type,
                "room": "Living Room",
                "topic": f"home/{device_type.lower().replace(' ', '_')}",
            },
        )
        assert response.status_code == 200, response.text
        body = response.json()
        assert body["type"] == device_type
        assert isinstance(body["type"], str)


def test_create_rejects_invalid_device_type(client):
    """An unknown device type must be rejected with HTTP 422."""
    response = client.post(
        "/devices/",
        json={
            "name": "Mystery Box",
            "type": "UnknownDevice",
            "room": "Attic",
            "topic": "home/mystery",
        },
    )
    assert response.status_code == 422
    assert "UnknownDevice" in response.text


def test_create_rejection_lists_allowed_values(client):
    """The 422 error message must mention the allowed device types."""
    response = client.post(
        "/devices/",
        json={
            "name": "Mystery Box",
            "type": "UnknownDevice",
            "room": "Attic",
            "topic": "home/mystery",
        },
    )
    detail = response.json()["detail"]
    for device_type in VALID_TYPES:
        assert device_type in str(detail)


def test_update_accepts_valid_device_type(client):
    """A supported device type must be accepted on update (200)."""
    created = client.post(
        "/devices/",
        json={
            "name": "Desk Lamp",
            "type": "Light",
            "room": "Office",
            "topic": "home/office/lamp",
        },
    )
    device_id = created.json()["id"]

    response = client.put(
        f"/devices/{device_id}",
        json={"type": "Smart Plug"},
    )
    assert response.status_code == 200, response.text
    assert response.json()["type"] == "Smart Plug"


def test_update_rejects_invalid_device_type(client):
    """An unknown device type must be rejected on update with HTTP 422."""
    created = client.post(
        "/devices/",
        json={
            "name": "Desk Lamp",
            "type": "Light",
            "room": "Office",
            "topic": "home/office/lamp",
        },
    )
    device_id = created.json()["id"]

def test_update_rejects_null_device_type(client):
    """An explicit null for ``type`` must be rejected with HTTP 422."""
    created = client.post(
        "/devices/",
        json={
            "name": "Desk Lamp",
            "type": "Light",
            "room": "Office",
            "topic": "home/office/lamp",
        },
    )
    device_id = created.json()["id"]

    response = client.put(
        f"/devices/{device_id}",
        json={"type": None},
    )
    assert response.status_code == 422


def test_update_without_type_keeps_existing_device(client):
    """An update payload without ``type`` must succeed (HTTP 200)."""
    created = client.post(
        "/devices/",
        json={
            "name": "Desk Lamp",
            "type": "Light",
            "room": "Office",
            "topic": "home/office/lamp",
        },
    )
    device_id = created.json()["id"]

    response = client.put(
        f"/devices/{device_id}",
        json={"room": "Kitchen"},
    )
    assert response.status_code == 200, response.text
    assert response.json()["type"] == "Light"
