from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class IncentiveType(Enumeration):
    """
The type of incentive offered (tax credit/rebate, tax deduction, tax waiver, subsidies, etc.).
    """
    type_: Literal['https://schema.org/IncentiveType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/IncentiveType'),serialization_alias='class') # type: ignore
