import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
from openai import OpenAI # openAIのchatGPTのAIを活用するための機能をインポート

api_key = st.secrets["openai"]["api_key"]
st.write(api_key)

client = OpenAI(api_key=api_key)
#client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a letter in Japanese."
        }
    ]
)

st.write(completion.choices[0].message.content)
