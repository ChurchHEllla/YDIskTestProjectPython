import requests

from utils.config import BASE_URL
from utils.secret import TOKEN_AUTH

class Client:
    """Клиент для управления ресурсами диска"""

    def __init__(self):
        self.base_url = BASE_URL
        self.url = "v1/disk/resources"
        self.fullPath = f"{self.base_url}/{self.url}"
        self.token = TOKEN_AUTH

    def create_resource(self, path: str):
        return requests.put(
            url=self.fullPath,
            headers={"Authorization": f"OAuth {self.token}"},
            params={
                "path": path,
                "fields": ""
            }
        )

    def delete_resource(self, path: str, isAsync: bool = False):
        return requests.delete(
            url=self.fullPath,
            headers={"Authorization": f"OAuth {self.token}"},
            params={
                "path": path,
                "permanently": "true",
                "force_async": "false" if not isAsync else "true",
            }
        )

    def get_resource(self, path: str):
        return requests.get(
            url=self.fullPath,
            headers={"Authorization": f"OAuth {self.token}"},
            params={
                "path": path,
            }
        )

    def copy_resource(self, fromPath: str, path: str, isAsync: bool = False):
        return requests.post(
            url=f"{self.fullPath}/copy",
            headers={"Authorization": f"OAuth {self.token}"},
            params={
                "from": fromPath,
                "path": path,
                "force_async": "false" if not isAsync else "true",
            }
        )

