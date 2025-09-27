from typing import Literal
from pydantic import Field
from schemaorg_models.place import Place


class AdministrativeArea(Place):
    """
A geographical region, typically under the jurisdiction of a particular government.
    """
    class_: Literal['https://schema.org/AdministrativeArea'] = Field(default='https://schema.org/AdministrativeArea', alias='@type', serialization_alias='@type') # type: ignore
