from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MediaEnumeration(Enumeration):
    """
MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination.
    """
    class_: Literal['https://schema.org/MediaEnumeration'] = Field(default='https://schema.org/MediaEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
