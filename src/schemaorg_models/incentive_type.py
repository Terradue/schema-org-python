from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveType(Enumeration):
    """
The type of incentive offered (tax credit/rebate, tax deduction, tax waiver, subsidies, etc.).
    """
    type_: Literal['https://schema.org/IncentiveType'] = Field(default='https://schema.org/IncentiveType', alias='@type', serialization_alias='@type') # type: ignore
