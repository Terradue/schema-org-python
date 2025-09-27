from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveType(Enumeration):
    """
The type of incentive offered (tax credit/rebate, tax deduction, tax waiver, subsidies, etc.).
    """
    class_: Literal['https://schema.org/IncentiveType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
