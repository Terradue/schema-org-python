from typing import Literal
from pydantic import Field
from schemaorg_models.insert_action import InsertAction


class PrependAction(InsertAction):
    """
The act of inserting at the beginning if an ordered collection.
    """
    type_: Literal['https://schema.org/PrependAction'] = Field(default='https://schema.org/PrependAction', alias='@type', serialization_alias='@type') # type: ignore
