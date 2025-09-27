from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MediaEnumeration(Enumeration):
    """
MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination.
    """
    type_: Literal['https://schema.org/MediaEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MediaEnumeration'),serialization_alias='class') # type: ignore
