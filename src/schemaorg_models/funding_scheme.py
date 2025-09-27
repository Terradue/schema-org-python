from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class FundingScheme(Organization):
    """
A FundingScheme combines organizational, project and policy aspects of grant-based funding
    that sets guidelines, principles and mechanisms to support other kinds of projects and activities.
    Funding is typically organized via [[Grant]] funding. Examples of funding schemes: Swiss Priority Programmes (SPPs); EU Framework 7 (FP7); Horizon 2020; the NIH-R01 Grant Program; Wellcome institutional strategic support fund. For large scale public sector funding, the management and administration of grant awards is often handled by other, dedicated, organizations - [[FundingAgency]]s such as ERC, REA, ...
    """
    type_: Literal['https://schema.org/FundingScheme'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FundingScheme'),serialization_alias='class') # type: ignore
