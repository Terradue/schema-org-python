from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class OnlineBusiness(Organization):
    """
A particular online business, either standalone or the online part of a broader organization. Examples include an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping provider, an online (virtual) doctor, etc.
    """
    type_: Literal['https://schema.org/OnlineBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OnlineBusiness'),serialization_alias='class') # type: ignore
