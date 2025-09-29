from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .local_business import LocalBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .menu import Menu
    from .rating import Rating

class FoodEstablishment(LocalBusiness):
    '''
    A food-related business.

    Attributes:
        menu: Either the actual menu as a structured representation, as text, or a URL of the menu.
        starRating: An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        servesCuisine: The cuisine of the restaurant.
        acceptsReservations: Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings ```Yes``` or ```No```.
        hasMenu: Either the actual menu as a structured representation, as text, or a URL of the menu.
    '''
    class_: Literal['https://schema.org/FoodEstablishment'] = Field( # type: ignore
        default='https://schema.org/FoodEstablishment',
        alias='@type',
        serialization_alias='@type'
    )
    menu: Optional[Union['Menu', List['Menu'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'menu',
            'https://schema.org/menu'
        ),
        serialization_alias='https://schema.org/menu'
    )
    starRating: Optional[Union['Rating', List['Rating']]] = Field(
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
    hasMenu: Optional[Union[HttpUrl, List[HttpUrl], 'Menu', List['Menu'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenu',
            'https://schema.org/hasMenu'
        ),
        serialization_alias='https://schema.org/hasMenu'
    )
