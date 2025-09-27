from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class HealthAspectEnumeration(Enumeration):
    """
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].
    """
    type_: Literal['https://schema.org/HealthAspectEnumeration'] = Field(default='https://schema.org/HealthAspectEnumeration', alias='@type', serialization_alias='@type') # type: ignore
