from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class GovernmentBenefitsType(Enumeration):
    """
GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.
    """
    type_: Literal['https://schema.org/GovernmentBenefitsType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GovernmentBenefitsType'),serialization_alias='class') # type: ignore
