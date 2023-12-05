from fastapi.testclient import TestClient
from fastapi import status
from src.app.main import app
import pytest
import base64
import os


client = TestClient(app)
pytest_plugins = ["dotenv"]


# Generates authorization headers using environment variables
def get_auth_headers():
    username = os.getenv("USERID")
    password = os.getenv("PASSWORD")
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded_credentials}"}


# Tests a valid calculation of mutual fund profit
def test_calculate_mutual_fund_profit():
    headers = get_auth_headers()

    response = client.get(
        "/profit",
        params={
            "scheme_code": "101209",
            "start_date": "26-07-2023",
            "end_date": "18-10-2023",
            "capital": 100000,
        },
        headers=headers
    )

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["net_profit"]


# Tests when input is invalid, expects status code 422
def test_invalid_input():
    headers = get_auth_headers()

    response = client.get("/profit", headers=headers)
    assert response.status_code == 422


# Tests scenario where scheme code is not found, expects status code 404
def test_scheme_code_not_found():
    headers = get_auth_headers()

    response = client.get(
        "/profit",
        params={
            "scheme_code": "12345",
            "start_date": "26-07-2023",
            "end_date": "18-10-2023",
            "capital": 100000,
        },
        headers=headers
    )
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == "Scheme code not found"


# Tests scenario where an invalid date format is provided, expects status code 400
def test_invalid_date_exception():
    headers = get_auth_headers()

    response = client.get(
        "/profit",
        params={
            "scheme_code": "101206",
            "start_date": "30-02-2023",
            "end_date": "18-10-2023",
            "capital": 100000,
        },
        headers=headers
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Invalid date"}



