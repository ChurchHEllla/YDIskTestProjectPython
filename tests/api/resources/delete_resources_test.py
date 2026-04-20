import pytest
import client.resources.client as cli
import model.resources.response.response as model


@pytest.mark.resources
def test_delete_folder_ok():

    folderName = ("Music18"
                  "")
    client = cli.Client()
    #Создаем папку
    client.create_resource(f"/{folderName}")

    #Удаляем папку
    response = client.delete_resource(f"/{folderName}", False)
    assert response.status_code == 204

    #Проверяем негативный сценарий Not Found и отсутствие папки
    response = client.delete_resource(f"/{folderName}", False)
    assert  response.status_code == 404, "Папка не удалена"