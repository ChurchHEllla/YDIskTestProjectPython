import pytest
import client.resources.client as cli
import model.resources.response.response as model

@pytest.mark.usefixtures("delete_resource")
@pytest.mark.resources
def test_copy_folder_ok():
    folderName = "Music6"
    folderCopyName = "Music7"

    client = cli.Client()

    #Создаем папку
    client.create_resource(f"/{folderName}")

    #Копируем созданную папку
    response = client.copy_resource(f"/{folderName}", f"/{folderCopyName}", False)
    assert response.status_code == 201

    #Проверяем что папка создалась
    response = client.get_resource(f"/{folderCopyName}")
    data = model.Item.model_validate(response.json())
    assert data.name == folderCopyName, "Имя созданной папки некорректно"

