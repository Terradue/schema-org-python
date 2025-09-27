from typing import Literal
from pydantic import Field
from schemaorg_models.organize_action import OrganizeAction


class ApplyAction(OrganizeAction):
    """
The act of registering to an organization/service without the guarantee to receive it.\
\
Related actions:\
\
* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.
    """
    type_: Literal['https://schema.org/ApplyAction'] = Field(default='https://schema.org/ApplyAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
