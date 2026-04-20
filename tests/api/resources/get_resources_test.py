import pytest
import client.resources.client as cli
import model.resources.response.response as model


@pytest.mark.usefixtures("delete_resource")
@pytest.mark.resources
def test_get_folder_ok():

    folderName = "Music18"

    client = cli.Client()
    client.create_resource(f"/{folderName}")

    response = client.get_resource(f"/{folderName}")
    assert response.status_code == 200

    data = model.Item.model_validate(response.json())
    assert data.name == folderName, "Имя созданной папки некорректно"