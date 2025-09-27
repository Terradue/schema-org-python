from typing import Literal
from pydantic import Field
from schemaorg_models.therapeutic_procedure import TherapeuticProcedure


class PsychologicalTreatment(TherapeuticProcedure):
    """
A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.
    """
    class_: Literal['https://schema.org/PsychologicalTreatment'] = Field(default='https://schema.org/PsychologicalTreatment', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
