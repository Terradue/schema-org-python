from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.dataset import Dataset

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
from schemaorg_models.data_feed_item import DataFeedItem
from schemaorg_models.thing import Thing

class DataFeed(Dataset):
    """
A single feed providing structured information about one or more entities or topics.
    """
    class_: Literal['https://schema.org/DataFeed'] = Field( # type: ignore
        default='https://schema.org/DataFeed',
        alias='@type',
        serialization_alias='@type'
    )
    dataFeedElement: Optional[Union[DataFeedItem, List[DataFeedItem], str, List[str], Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dataFeedElement',
            'https://schema.org/dataFeedElement'
        ),
        serialization_alias='https://schema.org/dataFeedElement'
    )
