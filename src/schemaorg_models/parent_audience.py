from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.people_audience import PeopleAudience


class ParentAudience(PeopleAudience):
    """
A set of characteristics describing parents, who can be interested in viewing some content.
    """
    type_: Literal['https://schema.org/ParentAudience'] = Field(default='https://schema.org/ParentAudience', alias='@type', serialization_alias='@type') # type: ignore
    childMaxAge: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('childMaxAge', 'https://schema.org/childMaxAge'), serialization_alias='https://schema.org/childMaxAge')
    childMinAge: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('childMinAge', 'https://schema.org/childMinAge'), serialization_alias='https://schema.org/childMinAge')
