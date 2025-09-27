from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """
The status of an Action.
    """
    class_: Literal['https://schema.org/ActionStatusType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
