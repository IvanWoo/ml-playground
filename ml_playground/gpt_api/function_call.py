import json
from openai import OpenAI


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


# Step 1, send model the user query and what functions it has access to
def run_conversation(prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        functions=[
            {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            }
        ],
        function_call="auto",
    )

    message = response.choices[0].message
    print(f"{message=}")

    # Step 2, check if the model wants to call a function
    if message.function_call:
        function_name = message.function_call.name
        function_args = json.loads(message.function_call.arguments)

        # Step 3, call the function
        # Note: the JSON response from the model may not be valid JSON
        function_response = get_current_weather(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )

        # Step 4, send model the info on the function call and function response
        second_response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        return second_response


for prompt in [
    "What's the weather like in Boston?",
    "东京的摄氏温度如何？",
    "What's the best sightseeing places in New York?",
]:
    print(prompt)
    print(f"{run_conversation(prompt)=}")
    print("\n")
