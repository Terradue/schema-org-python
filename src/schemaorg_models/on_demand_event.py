from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.publication_event import PublicationEvent


class OnDemandEvent(PublicationEvent):
    """
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """
    type_: Literal['https://schema.org/OnDemandEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OnDemandEvent'),serialization_alias='class') # type: ignore
