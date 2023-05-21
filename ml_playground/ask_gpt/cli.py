import os
from functools import partial

import click
import openai

from ml_playground.ask_gpt.prompt import Template, get_template

click.option = partial(click.option, show_default=True)
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0, stream=True):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=stream,
    )
    if stream:
        return response
    return response.choices[0].message["content"]


def compile_prompt(prompt, language, template):
    _template = get_template(template)
    return _template.format(prompt=prompt, language=language) if _template else prompt


@click.command()
@click.argument("prompt", required=True)
@click.option("--model", default="gpt-3.5-turbo", help="Model of GPT.")
@click.option(
    "--temperature", default=0.8, help="Degree of randomness of the model's output."
)
@click.option("--stream", default=True, help="Stream the GPT response.")
@click.option(
    "--template",
    type=click.Choice([t.value for t in Template]),
    help="Prompt template.",
)
@click.option("--language", default="English", help="Target language of answers.")
def main(prompt, model, temperature, stream, template, language):
    _prompt = compile_prompt(prompt, language, template)
    response = get_completion(
        _prompt,
        model,
        temperature,
        stream,
    )

    print(f"提问: {_prompt}\n")
    print("gpt 回答: ", end="")
    if stream:
        for chunk in response:
            if content := chunk["choices"][0].get("delta").get("content"):
                print(content, end="", flush=True)
    else:
        print(response)


if __name__ == "__main__":
    main()
