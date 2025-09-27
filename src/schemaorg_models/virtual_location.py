from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class VirtualLocation(Intangible):
    """
An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.
    """
    class_: Literal['https://schema.org/VirtualLocation'] = Field(default='https://schema.org/VirtualLocation', alias='class', serialization_alias='class') # type: ignore
