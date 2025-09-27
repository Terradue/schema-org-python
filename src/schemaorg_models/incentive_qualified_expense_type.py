from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveQualifiedExpenseType(Enumeration):
    """
The types of expenses that are covered by the incentive. For example some incentives are only for the goods (tangible items) but the services (labor) are excluded.
    """
    class_: Literal['https://schema.org/IncentiveQualifiedExpenseType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
