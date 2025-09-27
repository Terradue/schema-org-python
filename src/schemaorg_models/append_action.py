from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.insert_action import InsertAction


class AppendAction(InsertAction):
    """
The act of inserting at the end if an ordered collection.
    """
    type_: Literal['https://schema.org/AppendAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AppendAction'),serialization_alias='class') # type: ignore
