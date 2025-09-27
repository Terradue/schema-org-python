from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.review import Review


class ClaimReview(Review):
    """
A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).
    """
    class_: Literal['https://schema.org/ClaimReview'] = Field(default='https://schema.org/ClaimReview', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    claimReviewed: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('claimReviewed', 'https://schema.org/claimReviewed'), serialization_alias='https://schema.org/claimReviewed')
