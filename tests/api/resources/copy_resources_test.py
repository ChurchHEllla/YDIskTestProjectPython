import pytest
import client.resources.client as cli
import model.resources.response.response as model

@pytest.mark.usefixtures("delete_resource")
@pytest.mark.resources
def test_copy_folder_ok():
    client = cli.Client()

    #Создаем папку
    client.create_resource("/Music6")

    #Копируем созданную папку
    response = client.copy_resource("/Music6", "/Music7", False)
    assert response.status_code == 201

    #Проверяем что папка создалась
    client.get_resource("/Music7")
    data = model.Item.model_validate(response.json())
    assert data.name == "Music7", "Имя созданной папки некорректно"

