import pytest
import client.resources.client as cli
import model.resources.response.response as model

@pytest.mark.usefixtures("delete_resource")
@pytest.mark.resources
def test_create_folder_ok():

    folderName = "Music18"

    client = cli.Client()

    #Создаем папку
    response = client.create_resource(f"/{folderName}")
    assert response.status_code == 201

    #Проверяем корректность созданной папки
    response = client.get_resource(f"/{folderName}")
    data = model.Item.model_validate(response.json())
    assert data.name == folderName, "Папка создалась с некорректным названием"