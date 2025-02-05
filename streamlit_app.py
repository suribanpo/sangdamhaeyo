import streamlit as st
import seaborn as sns


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = sns.load_dataset("penguins")
df