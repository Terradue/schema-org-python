from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.play_action import PlayAction

from schemaorg_models.entertainment_business import EntertainmentBusiness

class PerformAction(PlayAction):
    """
The act of participating in performance arts.
    """
    class_: Literal['https://schema.org/PerformAction'] = Field(default='https://schema.org/PerformAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    entertainmentBusiness: Optional[Union[EntertainmentBusiness, List[EntertainmentBusiness]]] = Field(default=None, validation_alias=AliasChoices('entertainmentBusiness', 'https://schema.org/entertainmentBusiness'), serialization_alias='https://schema.org/entertainmentBusiness')
