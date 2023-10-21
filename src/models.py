from pydantic import Field
from instructor import OpenAISchema
from enum import Enum
from typing import List


class EntityType(OpenAISchema):
    name: str = Field(..., description="Name of the entity type.")
    description: str = Field(..., description="Description of the entity type.")
    examples: List[str] = Field(..., description="List of examples of the entity type.")


class EntityTypeSuggestionsOutput(OpenAISchema):
    entity_types: List[EntityType] = Field(
        ...,
        description="""List of entity types suggested. Entity type name should be all uppercase 
        and separated by underscores (i.e. PERSON, LOCATION, PHONE_NUMBER, etc.""",
    )


class Entity(OpenAISchema):
    start: int = Field(
        ...,
        alias="start_pos",
        description="The starting position of the entity in the text.",
    )
    end: int = Field(
        ...,
        alias="end_pos",
        description="The ending position of the entity in the text.",
    )
    label: str = Field(..., description="The label of the entity.")
    text: str = Field(..., description="The text of the entity.")


class NEROutput(OpenAISchema):
    entities: List[Entity] = Field(
        ..., description="The list of entities found in the text."
    )


class Nli(Enum):
    contradiction = "contradiction"
    neutral = "neutral"
    entailment = "entailment"


class NliOutput(OpenAISchema):
    explanation: str = Field(
        ..., description="Think step by step whether the premise entails the hypothesis"
    )
    label: Nli = Field(..., description="The label of the text.")
