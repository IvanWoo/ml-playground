import os
import click

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0, stream=True):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=stream,
    )
    if not stream:
        return response.choices[0].message["content"]
    return response


@click.command()
@click.argument("prompt", required=True)
@click.option("--model", default="gpt-3.5-turbo", help="Model of GPT.")
@click.option(
    "--temperature", default=0.8, help="Degree of randomness of the model's output"
)
@click.option("--stream", default=True, help="Stream the GPT response.")
def main(prompt, model, temperature, stream):
    response = get_completion(prompt, model, temperature, stream)
    if not stream:
        print(response)
    else:
        for chunk in response:
            if content := chunk["choices"][0].get("delta").get("content"):
                print(content, end="", flush=True)


if __name__ == "__main__":
    main()
