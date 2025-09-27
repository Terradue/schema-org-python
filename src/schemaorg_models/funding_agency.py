from typing import Literal
from pydantic import Field
from schemaorg_models.project import Project


class FundingAgency(Project):
    """
A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages
    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).
    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.
    
Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ...
    
    """
    class_: Literal['https://schema.org/FundingAgency'] = Field(default='https://schema.org/FundingAgency', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
