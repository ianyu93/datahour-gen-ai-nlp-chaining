import os
import openai
import requests
from typing import List, Optional

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_completion_request(
    model: str = "gpt-3.5-turbo-0613",
    temperature: int = 0,
    messages: List[dict] = None,
    functions: List[dict] = None,
    function_call: str = None,
):
    if messages is None:
        messages = [{"role": "user", "content": "Hello, how are you?"}]
    return openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        functions=functions,
        function_call=function_call,
        messages=messages,
    )
