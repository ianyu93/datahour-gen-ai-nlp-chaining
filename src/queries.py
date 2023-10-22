from typing import List

from . import models
from .logger import setup_logger
from .utils import chat_completion_request

logger = setup_logger(__name__, formatter="verbose")


def entity_type_suggestions(
    persona: str,
    purpose: str,
) -> List[models.EntityType]:
    """Generate a list of named entity types that specifically relate to the persona and the purpose.

    Args:
        persona: Persona of the user, e.g. "student", "teacher", "journalist", etc.
        purpose: Purpose of the named entity types to be generated, e.g. "to help the user",
        "to help the user understand the text", etc.

    Returns:
        List of named entity types with name, description, and examples.
    """
    messages = [
        {
            "role": "user",
            "content": f"""
You are given a persona and a purpose. Act as the persona, understand the persona's goal, and generate a list of named
entity types that specifically relate to the persona and the purpose. Consider the following context:
Persona: {persona}
Purpose: {purpose}
 """,
        }
    ]
    functions = [models.EntityTypeSuggestionsOutput.openai_schema]
    function_call = {"name": models.EntityTypeSuggestionsOutput.openai_schema["name"]}
    response = chat_completion_request(
        messages=messages, functions=functions, function_call=function_call
    )
    logger.info(f"Response: {response}")
    return models.EntityTypeSuggestionsOutput.from_response(response)


def ner(entity_types: List[models.EntityType], text: str) -> List[models.Entity]:
    """Extract named entities from a text given a list of entity types.

    Args:
        entity_types: List of entity types to extract from the text.
        text: Text to extract named entities from.

    Returns:
        List of named entities with start and end position, label, and text.
    """
    messages = [
        {
            "role": "user",
            "content": f"""
 You are a named entity recognition model.  Please be as strict as possible in your predictions.
 You are given a text, and you are to extract the following entity types: {entity_types}
 """,
        },
        {"role": "user", "content": f"Text: {text}"},
    ]
    functions = [models.NEROutput.openai_schema]
    function_call = {"name": models.NEROutput.openai_schema["name"]}
    response = chat_completion_request(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call=function_call,
    )
    return models.NEROutput.from_response(response)


def ner_data_quality_check(entity: models.Entity, text: str) -> List[models.NliOutput]:
    """Check the quality of a named entity extracted from a text.

    Args:
        entity: Named entity to check the quality of.
        text: Text that the named entity was extracted from.

    Returns:
        List of natural language inference labels with explanations.
    """
    messages = [
        {
            "role": "user",
            "content": f"""
Premise: Text: {text}
Hypothesis: The text contains {entity.label}: {entity.text}
""",
        },
        {
            "role": "user",
            "content": f"""
ENTITY Span: {entity.start} - {entity.end}
Entity Type: {entity.label}
Entity Value: {entity.text}
""",
        },
    ]

    functions = [models.NliOutput.openai_schema]
    function_call = {"name": models.NliOutput.openai_schema["name"]}
    response = chat_completion_request(
        messages=messages,
        functions=functions,
        function_call=function_call,
    )
    return models.NliOutput.from_response(response)
