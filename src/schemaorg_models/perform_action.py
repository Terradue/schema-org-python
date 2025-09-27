from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.play_action import PlayAction

from schemaorg_models.entertainment_business import EntertainmentBusiness

class PerformAction(PlayAction):
    """
The act of participating in performance arts.
    """
    type_: Literal['https://schema.org/PerformAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PerformAction'),serialization_alias='class') # type: ignore
    entertainmentBusiness: Optional[Union[EntertainmentBusiness, List[EntertainmentBusiness]]] = Field(default=None,validation_alias=AliasChoices('entertainmentBusiness', 'https://schema.org/entertainmentBusiness'),serialization_alias='https://schema.org/entertainmentBusiness')
