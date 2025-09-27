from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class Quotation(CreativeWork):
    """
A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]].
    """
    class_: Literal['https://schema.org/Quotation'] = Field(default='https://schema.org/Quotation', alias='@type', serialization_alias='@type') # type: ignore
    spokenByCharacter: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('spokenByCharacter', 'https://schema.org/spokenByCharacter'), serialization_alias='https://schema.org/spokenByCharacter')
