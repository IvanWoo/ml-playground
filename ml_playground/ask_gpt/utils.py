from openai import OpenAI

client = OpenAI()


def get_completion(prompt, model="gpt-4", temperature=0, stream=False):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=stream,
    )
    if stream:
        return response
    return response.choices[0].message.content
