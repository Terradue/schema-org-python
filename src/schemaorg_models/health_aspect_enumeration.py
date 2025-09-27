from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class HealthAspectEnumeration(Enumeration):
    """
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].
    """
    type_: Literal['https://schema.org/HealthAspectEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HealthAspectEnumeration'),serialization_alias='class') # type: ignore
