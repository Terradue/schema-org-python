from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class OnlineBusiness(Organization):
    """
A particular online business, either standalone or the online part of a broader organization. Examples include an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping provider, an online (virtual) doctor, etc.
    """
    type_: Literal['https://schema.org/OnlineBusiness'] = Field(default='https://schema.org/OnlineBusiness', alias='@type', serialization_alias='@type') # type: ignore
