from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.add_action import AddAction

from schemaorg_models.place import Place

class InsertAction(AddAction):
    """
The act of adding at a specific location in an ordered collection.
    """
    toLocation: Optional[Union[Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('toLocation', 'https://schema.org/toLocation'),serialization_alias='https://schema.org/toLocation')
