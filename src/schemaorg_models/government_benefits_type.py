from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class GovernmentBenefitsType(Enumeration):
    """
GovernmentBenefitsType enumerates several kinds of government benefits to support the COVID-19 situation. Note that this structure may not capture all benefits offered.
    """
    class_: Literal['https://schema.org/GovernmentBenefitsType'] = Field(default='https://schema.org/GovernmentBenefitsType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
