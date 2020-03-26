import pytest
from faker import Faker


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def authencticated_client(client, django_user_model):
    fake = Faker()
    username = fake.user_name()
    password = fake.text()
    u = django_user_model.objects.create_user(username=username, password=password)
    u.validado = True
    u.save()
    client.login(username=username, password=password)
    return client


@pytest.fixture
def fake_user(client, django_user_model):
    username = 'teste'
    password = 'teste'
    nome = 'teste'
    email = 'teste@teste.com'
    user = django_user_model.objects.create_user(username=username, password=password, validado=True, nome=nome,
                                                 email=email)
    client.login(username=username, password=password)
    return user
