from typing import Literal
from pydantic import Field
from schemaorg_models.publication_event import PublicationEvent


class OnDemandEvent(PublicationEvent):
    """
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """
    type_: Literal['https://schema.org/OnDemandEvent'] = Field(default='https://schema.org/OnDemandEvent', alias='@type', serialization_alias='@type') # type: ignore
