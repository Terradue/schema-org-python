from typing import Literal
from pydantic import Field
from schemaorg_models.place import Place


class AdministrativeArea(Place):
    """
A geographical region, typically under the jurisdiction of a particular government.
    """
    class_: Literal['https://schema.org/AdministrativeArea'] = Field('class', alias='class', serialization_alias='class') # type: ignore
