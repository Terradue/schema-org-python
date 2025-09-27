from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class PublicToilet(CivicStructure):
    """
A public toilet is a room or small building containing one or more toilets (and possibly also urinals) which is available for use by the general public, or by customers or employees of certain businesses.
    """
    class_: Literal['https://schema.org/PublicToilet'] = Field(default='https://schema.org/PublicToilet', alias='class', serialization_alias='class') # type: ignore
