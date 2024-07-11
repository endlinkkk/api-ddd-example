
from faker import Faker
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response

def test_create_claim_success(app: FastAPI, client: TestClient, faker: Faker):
    url = app.url_path_for('create_claim_handler')
    fake_title = faker.text(max_nb_chars=10)
    fake_message = faker.text()
    fake_username = faker.name()
    fake_email = faker.email(domain='gmail.com')
    fake_status = faker.text(max_nb_chars=10)

    response: Response = client.post(url=url, json={
        'title': fake_title,
        'message': fake_message,
        'username': fake_username,
        'email': fake_email,
        'status': fake_status,
    })

    assert response.is_success
    json_data = response.json()

    assert json_data['title'] == fake_title