from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """
The status of an Action.
    """
    type_: Literal['https://schema.org/ActionStatusType'] = Field(default='https://schema.org/ActionStatusType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
