from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class SearchAction(Action):
    """
The act of searching for an object.\
\
Related actions:\
\
* [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily.
    """
    type_: Literal['https://schema.org/SearchAction'] = Field(default='https://schema.org/SearchAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    query: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('query', 'https://schema.org/query'), serialization_alias='https://schema.org/query')
