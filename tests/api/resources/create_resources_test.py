import pytest
import client.resources.client as cli
import model.resources.response.response as model

@pytest.mark.usefixtures("delete_resource")
@pytest.mark.resources
def test_create_folder_ok():
    client = cli.Client()

    #Создаем папку
    response = client.create_resource("/Music18")
    assert response.status_code == 201

    #Проверяем корректность созданной папки
    response = client.get_resource("/Music18")
    data = model.Item.model_validate(response.json())
    assert data.name == "Music18", "Папка создалась с некорректным названием"