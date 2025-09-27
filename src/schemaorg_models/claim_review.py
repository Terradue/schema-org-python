from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.review import Review


class ClaimReview(Review):
    """
A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).
    """
    class_: Literal['https://schema.org/ClaimReview'] = Field(default='https://schema.org/ClaimReview', alias='class', serialization_alias='class') # type: ignore
    claimReviewed: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('claimReviewed', 'https://schema.org/claimReviewed'), serialization_alias='https://schema.org/claimReviewed')
