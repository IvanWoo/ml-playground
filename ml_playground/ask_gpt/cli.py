from functools import partial

import click

from ml_playground.ask_gpt.utils import get_completion
from ml_playground.ask_gpt.prompt import Template, get_template

click.option = partial(click.option, show_default=True)


def compile_prompt(prompt: str, language: str, template: str) -> str:
    if _template := get_template(template):
        return _template.format(prompt=prompt, language=language)
    return prompt


@click.command()
@click.argument("prompt", required=True)
@click.option("--model", default="gpt-4o", help="Model of GPT.")
@click.option(
    "--temperature", default=0.8, help="Degree of randomness of the model's output."
)
@click.option("--stream", default=True, is_flag=True, help="Stream the GPT response.")
@click.option(
    "-t",
    "--template",
    type=click.Choice([t.value for t in Template]),
    help="Prompt template.",
)
@click.option("-l", "--language", default="English", help="Target language of answers.")
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
            if content := chunk.choices[0].delta.content:
                print(content, end="", flush=True)
    else:
        print(response)


if __name__ == "__main__":
    main()
