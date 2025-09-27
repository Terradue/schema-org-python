from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.project import Project


class FundingAgency(Project):
    """
A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages
    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).
    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.
    
Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ...
    
    """
    type_: Literal['https://schema.org/FundingAgency'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FundingAgency'),serialization_alias='class') # type: ignore
