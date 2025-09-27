from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.local_business import LocalBusiness

from schemaorg_models.menu import Menu
from schemaorg_models.rating import Rating

class FoodEstablishment(LocalBusiness):
    """
A sub property of location. The specific food establishment where the action occurred.
    """
    class_: Literal['https://schema.org/FoodEstablishment'] = Field(default='https://schema.org/FoodEstablishment', alias='class', serialization_alias='class') # type: ignore
    menu: Optional[Union[Menu, List[Menu], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('menu', 'https://schema.org/menu'), serialization_alias='https://schema.org/menu')
    @field_serializer('menu')
    def menu2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    starRating: Optional[Union[Rating, List[Rating]]] = Field(default=None, validation_alias=AliasChoices('starRating', 'https://schema.org/starRating'), serialization_alias='https://schema.org/starRating')
    servesCuisine: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('servesCuisine', 'https://schema.org/servesCuisine'), serialization_alias='https://schema.org/servesCuisine')
    acceptsReservations: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('acceptsReservations', 'https://schema.org/acceptsReservations'), serialization_alias='https://schema.org/acceptsReservations')
    @field_serializer('acceptsReservations')
    def acceptsReservations2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    hasMenu: Optional[Union[HttpUrl, List[HttpUrl], Menu, List[Menu], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('hasMenu', 'https://schema.org/hasMenu'), serialization_alias='https://schema.org/hasMenu')
    @field_serializer('hasMenu')
    def hasMenu2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

