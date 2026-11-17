import pandas as pd
import streamlit as st

st.title("Ahmed Azab portfolio")

st.image("./images/images.jpg", alt="Sunrise over a mountain ridge", width=300)

st.write(
    "Welcome to my portfolio! Here you can find information about my projects, skills, and experience. Feel free to explore and reach out if you have any questions or opportunities for collaboration."
)

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)


if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old!")


df = pd.DataFrame(
    {
        "Project": ["Project A", "Project B", "Project C"],
        "Description": [
            "Description of Project A",
            "Description of Project B",
            "Description of Project C",
        ],
        "Link": [
            "  https://example.com/project-a",
            "https://example.com/project-b",
            "https://example.com/project-c",
        ],
    }
)

st.dataframe(df)
