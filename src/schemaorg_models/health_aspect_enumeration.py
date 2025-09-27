from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class HealthAspectEnumeration(Enumeration):
    """
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].
    """
    class_: Literal['https://schema.org/HealthAspectEnumeration'] = Field(default='https://schema.org/HealthAspectEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
