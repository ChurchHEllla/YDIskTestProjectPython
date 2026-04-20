import pytest
import client.resources.client as cli
import model.resources.response.response as model

#Чистим диск после завершения работы автотеста
@pytest.fixture(scope="session")
def delete_resource():
    yield
    client = cli.Client()
    response = client.get_resource("/")
    data = model.getModel.model_validate(response.json())
    if data.embedded.items:
        for item in data.embedded.items:
            client.delete_resource(f"/{item.name}", False)