from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.creative_work import CreativeWork

class Claim(CreativeWork):
    """
A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized with the [[text]] property. Variations on well known claims can have their common identity indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]] description includes enough contextual information to minimize the risk of ambiguity or inclarity. In practice, many claims are better understood in the context in which they appear or the interpretations provided by claim reviews.

  Beyond [[ClaimReview]], the Claim type can be associated with related creative works - for example a [[ScholarlyArticle]] or [[Question]] might be [[about]] some [[Claim]].

  At this time, Schema.org does not define any types of relationship between claims. This is a natural area for future exploration.
  
    """
    type_: Literal['https://schema.org/Claim'] = Field(default='https://schema.org/Claim', alias='@type', serialization_alias='@type') # type: ignore
    claimInterpreter: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('claimInterpreter', 'https://schema.org/claimInterpreter'), serialization_alias='https://schema.org/claimInterpreter')
    firstAppearance: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('firstAppearance', 'https://schema.org/firstAppearance'), serialization_alias='https://schema.org/firstAppearance')
    appearance: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('appearance', 'https://schema.org/appearance'), serialization_alias='https://schema.org/appearance')
