from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.assess_action import AssessAction

from schemaorg_models.review import Review

class ReviewAction(AssessAction):
    """
The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.
    """
    class_: Literal['https://schema.org/ReviewAction'] = Field(default='https://schema.org/ReviewAction', alias='@type', serialization_alias='@type') # type: ignore
    resultReview: Optional[Union[Review, List[Review]]] = Field(default=None, validation_alias=AliasChoices('resultReview', 'https://schema.org/resultReview'), serialization_alias='https://schema.org/resultReview')
