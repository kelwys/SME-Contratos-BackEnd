import pytest
from rest_framework import status

# pytestmark = pytest.mark.django_db

# TODO Teste falhando por incompatibilidade do pytest com JSONFild
# def test_url_unauthorized(client):
#     response = client.get('/colunas-contrato/')
#     assert response.status_code == status.HTTP_401_UNAUTHORIZED
#
#
# def test_url_authorized(authencticated_client):
#     response = authencticated_client.get('/colunas-contrato/')
#     assert response.status_code == status.HTTP_200_OK
