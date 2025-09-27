from typing import Literal
from pydantic import Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Vessel(AnatomicalStructure):
    """
A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.
    """
    class_: Literal['https://schema.org/Vessel'] = Field(default='https://schema.org/Vessel', alias='class', serialization_alias='class') # type: ignore
