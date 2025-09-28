from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.legislation import Legislation

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.legal_value_level import LegalValueLevel

class LegislationObject(Legislation):
    """
A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.
    """
    class_: Literal['https://schema.org/LegislationObject'] = Field( # type: ignore
        default='https://schema.org/LegislationObject',
        alias='@type',
        serialization_alias='@type'
    )
    legislationLegalValue: Optional[Union[LegalValueLevel, List[LegalValueLevel]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationLegalValue',
            'https://schema.org/legislationLegalValue'
        ),
        serialization_alias='https://schema.org/legislationLegalValue'
    )
