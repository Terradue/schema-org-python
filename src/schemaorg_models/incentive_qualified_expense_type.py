from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class IncentiveQualifiedExpenseType(Enumeration):
    """
The types of expenses that are covered by the incentive. For example some incentives are only for the goods (tangible items) but the services (labor) are excluded.
    """
    type_: Literal['https://schema.org/IncentiveQualifiedExpenseType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/IncentiveQualifiedExpenseType'),serialization_alias='class') # type: ignore
