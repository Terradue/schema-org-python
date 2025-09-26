from typing import Union, List, Optional
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
    query: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('query', 'https://schema.org/query'),serialization_alias='https://schema.org/query')
