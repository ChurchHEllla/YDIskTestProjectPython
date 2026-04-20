import pytest
import client.resources.client as cli
import model.resources.response.response as model


@pytest.mark.usefixtures("delete_resource")
@pytest.mark.resources
def test_get_folder_ok():
    client = cli.Client()
    client.create_resource("/Music18")

    response = client.get_resource("/Music18")
    assert response.status_code == 200

    data = model.Item.model_validate(response.json())
    assert data.name == "Music18", "Имя созданной папки некорректно"