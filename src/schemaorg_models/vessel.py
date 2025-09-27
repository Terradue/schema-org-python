from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Vessel(AnatomicalStructure):
    """
A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.
    """
    type_: Literal['https://schema.org/Vessel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Vessel'),serialization_alias='class') # type: ignore
