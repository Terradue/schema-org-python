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
    class_: Literal['https://schema.org/ApplyAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
