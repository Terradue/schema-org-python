from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.web_content import WebContent

from schemaorg_models.health_aspect_enumeration import HealthAspectEnumeration

class HealthTopicContent(WebContent):
    """
[[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic, e.g. a condition, its symptoms or treatments. Such content may be comprised of several parts or sections and use different types of media. Multiple instances of [[WebContent]] (and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]] where there is some kind of content hierarchy, and their content described with [[about]] and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.
  
    """
    class_: Literal['https://schema.org/HealthTopicContent'] = Field(default='https://schema.org/HealthTopicContent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    hasHealthAspect: Optional[Union[HealthAspectEnumeration, List[HealthAspectEnumeration]]] = Field(default=None, validation_alias=AliasChoices('hasHealthAspect', 'https://schema.org/hasHealthAspect'), serialization_alias='https://schema.org/hasHealthAspect')
