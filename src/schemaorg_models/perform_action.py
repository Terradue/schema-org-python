from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.play_action import PlayAction

from schemaorg_models.entertainment_business import EntertainmentBusiness

class PerformAction(PlayAction):
    """
The act of participating in performance arts.
    """
    entertainmentBusiness: Optional[Union[EntertainmentBusiness, List[EntertainmentBusiness]]] = Field(default=None,validation_alias=AliasChoices('entertainmentBusiness', 'https://schema.org/entertainmentBusiness'),serialization_alias='https://schema.org/entertainmentBusiness')
