from typing import Literal
from pydantic import Field
from schemaorg_models.publication_event import PublicationEvent


class OnDemandEvent(PublicationEvent):
    """
A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """
    class_: Literal['https://schema.org/OnDemandEvent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
