from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work_series import CreativeWorkSeries


class Periodical(CreativeWorkSeries):
    """
A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.\
\
See also [blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """
    type_: Literal['https://schema.org/Periodical'] = Field(default='https://schema.org/Periodical', alias='@type', serialization_alias='@type') # type: ignore
