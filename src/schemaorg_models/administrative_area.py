from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class AdministrativeArea(Place):
    """
A geographical region, typically under the jurisdiction of a particular government.
    """
    type_: Literal['https://schema.org/AdministrativeArea'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AdministrativeArea'),serialization_alias='class') # type: ignore
