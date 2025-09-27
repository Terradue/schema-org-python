from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """
The status of an Action.
    """
    type_: Literal['https://schema.org/ActionStatusType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ActionStatusType'),serialization_alias='class') # type: ignore
