from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.review import Review


class ClaimReview(Review):
    """
A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).
    """
    claimReviewed: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('claimReviewed', 'https://schema.org/claimReviewed'),serialization_alias='https://schema.org/claimReviewed')
