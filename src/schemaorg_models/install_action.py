from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class InstallAction(ConsumeAction):
    """
The act of installing an application.
    """
    class_: Literal['https://schema.org/InstallAction'] = Field(default='https://schema.org/InstallAction', alias='class', serialization_alias='class') # type: ignore
