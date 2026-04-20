from pydantic import BaseModel, Field
from typing import List, Dict, Optional

#Модели ответов ручек
class Item(BaseModel):
    path: str
    type: str
    name: str
    created: Optional[str] = None
    modified: Optional[str] = None
    resource_id: str
    revision: int
    comment_ids: Dict[str, str]
    exif: Dict

class Embedded(BaseModel):
    path: str
    limit: int
    offset: int
    sort: str
    total: int
    items: List[Item]

class getModel(BaseModel):
    """Модель ответа для запроса ресурсов из корневой папки"""
    path: str
    type: str
    name: str
    created: Optional[str] = None
    modified: Optional[str] = None
    embedded: Embedded = Field(alias="_embedded")
    resource_id: str
    revision: int
    comment_ids: Dict
    exif: Dict

    class Config:
        populate_by_name = True

class createModel(BaseModel):
    """Модель ответа создания ресурсов"""
    href: str
    method: str
    templated: bool