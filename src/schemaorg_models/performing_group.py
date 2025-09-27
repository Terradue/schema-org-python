from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class PerformingGroup(Organization):
    """
A performance group, such as a band, an orchestra, or a circus.
    """
    class_: Literal['https://schema.org/PerformingGroup'] = Field('class', alias='class', serialization_alias='class') # type: ignore
