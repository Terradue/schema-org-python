from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MediaEnumeration(Enumeration):
    """
MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination.
    """
    class_: Literal['https://schema.org/MediaEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
