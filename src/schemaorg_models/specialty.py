from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class Specialty(Enumeration):
    """
One of the domain specialities to which this web page's content applies.
    """
    class_: Literal['https://schema.org/Specialty'] = Field(default='https://schema.org/Specialty', alias='@type', serialization_alias='@type') # type: ignore
