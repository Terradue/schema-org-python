from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.local_business import LocalBusiness

from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.menu import Menu
from schemaorg_models.rating import Rating

class FoodEstablishment(LocalBusiness):
    """
A sub property of location. The specific food establishment where the action occurred.
    """
    class_: Literal['https://schema.org/FoodEstablishment'] = Field( # type: ignore
        default='https://schema.org/FoodEstablishment',
        alias='@type',
        serialization_alias='@type'
    )
    menu: Optional[Union[Menu, List[Menu], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'menu',
            'https://schema.org/menu'
        ),
        serialization_alias='https://schema.org/menu'
    )
    starRating: Optional[Union[Rating, List[Rating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'starRating',
            'https://schema.org/starRating'
        ),
        serialization_alias='https://schema.org/starRating'
    )
    servesCuisine: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'servesCuisine',
            'https://schema.org/servesCuisine'
        ),
        serialization_alias='https://schema.org/servesCuisine'
    )
    acceptsReservations: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptsReservations',
            'https://schema.org/acceptsReservations'
        ),
        serialization_alias='https://schema.org/acceptsReservations'
    )
    hasMenu: Optional[Union[HttpUrl, List[HttpUrl], Menu, List[Menu], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenu',
            'https://schema.org/hasMenu'
        ),
        serialization_alias='https://schema.org/hasMenu'
    )
