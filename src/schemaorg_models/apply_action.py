from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organize_action import OrganizeAction


class ApplyAction(OrganizeAction):
    """
The act of registering to an organization/service without the guarantee to receive it.\
\
Related actions:\
\
* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.
    """
    type_: Literal['https://schema.org/ApplyAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ApplyAction'),serialization_alias='class') # type: ignore
