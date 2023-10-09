import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

template = """
    Below is an email that is not globalized.
    Your goal is to:
    1. Properly format the email
    2. Convert the input text to the selected dialect
    3. Convert the input text to the selected tone
    
    Here are some examples of different Tones:
    - Formal: "Dear Sir or Madam, I am writing to you to inform you of the recent changes to our company."
    - Informal: "Hey, I'm writing to you to let you know about the recent changes to our company."
    
    Here are some examples of different Dialects:
    - American: "I am writing to you to inform you of the recent changes to our company."
    - British: "I am writing to you to inform you of the recent changes to our company."
    - French: "Je vous écris pour vous informer des récents changements au sein de notre entreprise."
    - Chinese: "我写信给你，告诉你我们公司最近的变化。"
    - Cantonese: "我寫信俾你，話你我哋公司最近嘅變化。"
    
    Below is the email, tone and the dialect:
    TONE: {tone}\n
    DIALECT: {dialect}\n
    EMAIL: {email}\n
    
    YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template
)


def load_LLM():
    return OpenAI(temperature=0.5)


llm = load_LLM()

st.set_page_config(page_title="Globalize Email", page_icon="📧", layout="wide")
st.header("Globalize Text")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Often professionals would like to improve thier emails, but don't have the time to do so. This app "
                "will help you improve your emails by making them more globalized.")

# with col2:
#     st.image(image='TweetScreenshot.png', caption='Example of a globalized email', width=500)

st.markdown("## Enter your email below")

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox('Tone', ('Formal', 'Informal'))

with col2:
    option_dialect = st.selectbox('Dialect', ('American', 'British', 'French', 'Chinese', 'Cantonese'))


def get_text():
    input_text = st.text_area(label='', value='', height=300, key="email_input")
    return input_text


email_input = get_text()

st.markdown("### Converted Email")

if email_input:
    prompt_with_email = prompt.format(
        tone=option_tone,
        dialect=option_dialect,
        email=email_input
    )
    formatted_email = llm(prompt_with_email)
    st.write(formatted_email)
