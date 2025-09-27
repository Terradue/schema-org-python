from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.property import Property

class ConstraintNode(Intangible):
    """
The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]]. These constraint properties can serve a
    variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values.
    """
    class_: Literal['https://schema.org/ConstraintNode'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    numConstraints: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numConstraints', 'https://schema.org/numConstraints'), serialization_alias='https://schema.org/numConstraints')
    constraintProperty: Optional[Union[HttpUrl, List[HttpUrl], Property, List[Property]]] = Field(default=None,validation_alias=AliasChoices('constraintProperty', 'https://schema.org/constraintProperty'), serialization_alias='https://schema.org/constraintProperty')
    @field_serializer('constraintProperty')
    def constraintProperty2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

