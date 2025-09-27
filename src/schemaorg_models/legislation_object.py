from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.legislation import Legislation

from schemaorg_models.legal_value_level import LegalValueLevel

class LegislationObject(Legislation):
    """
A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.
    """
    type_: Literal['https://schema.org/LegislationObject'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LegislationObject'),serialization_alias='class') # type: ignore
    legislationLegalValue: Optional[Union[LegalValueLevel, List[LegalValueLevel]]] = Field(default=None,validation_alias=AliasChoices('legislationLegalValue', 'https://schema.org/legislationLegalValue'),serialization_alias='https://schema.org/legislationLegalValue')
