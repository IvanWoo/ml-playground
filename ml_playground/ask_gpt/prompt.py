from enum import Enum
from typing import Optional

template_socratic_questioning = """
Your task is to automatically take turns asking and answering questions. We'll begin with an initial question. Then go on answering and asking in this pattern:
Question: The initial question
Answer: The answer to the initial question
Question: The question about the reason for the previous answer
Answer: The answer to the previous question
Question:
Keep asking about the origin of the thinking, alternative viewpoints and perspectives and conflicts between contentions, exploring implications and consequences, questioning the question for the last answer. Stop only when the answer is "That's the way it is" or "We don't know for now". Each question and answer should be a single sentence with no more than 20 words. Add "Q: " before each question and "A: " before each answer.

Ask and answer in {language} regardless of the language I use. Don't show the translation process. Just write questions and answers in the destination language.

Now, the initial question is: '{prompt}'
"""

template_three_questions = """
Whenever I ask you about a piece of knowledge, you should raise three questions and try to answer these three questions.
These three questions should be asked according to the following ideas:
1. Where does it come from? This question implies that the emergence of knowledge is not created out of thin air; it must have been born to solve a problem.
2. What is it? This question implies what kind of knowledge it is itself. What solutions does it propose for the problem it aims to solve?
3. Where is it going? This question implies what flaws exist in the knowledge itself regarding the resolution of the problem? What are its limitations? What is the future direction of development?

Ask and answer in {language} regardless of the language I use. Don't show the translation process. Just write questions and answers in the destination language.

Now, the initial question is: '{prompt}'
"""

template_jp_tutor = """
You are Japanese language teacher. Whenever I ask you about a Japaneses snippet, you should explain the sentence structure, grammar and thesaurus with at least six examples from literature, lyrics or newspaper.

Answer in {language} regardless of the language I use. Don't show the translation process. Just response in the destination language.

Now, here is the Japanese snippet: '{prompt}'
"""

template_translate = """
Your task is to translate the given text into {language}. Provide the translation directly without any additional commentary or explanation.

Translate the following text: '{prompt}'
"""


class Template(Enum):
    SOCRATIC = "socratic"
    THREE = "three"
    JP_TUTOR = "jp_tutor"
    TRANSLATE = "translate"


template_map = {
    Template.SOCRATIC.value: template_socratic_questioning,
    Template.THREE.value: template_three_questions,
    Template.JP_TUTOR.value: template_jp_tutor,
    Template.TRANSLATE.value: template_translate,
}


def get_template(name: str) -> Optional[str]:
    return template_map.get(name)
