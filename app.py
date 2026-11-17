import pandas as pd
import streamlit as st
import torch
from transformers import pipeline

pipe = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")

# pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
model = AutoModelForSequenceClassification.from_pretrained(
    "SamLowe/roberta-base-go_emotions", device_map="auto"
)


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


sentences = ["I am not having a great day"]

# Tokenize the input sentences
inputs = tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)

# Move inputs to the same device as the model
inputs = {k: v.to(model.device) for k, v in inputs.items()}

# Get predictions from the model
with torch.no_grad():
    outputs = model(**inputs)

# Extract and print raw logits
print("Logits:", outputs.logits)

# Apply softmax to get probabilities
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
print("Probabilities:", probabilities)

# Get the class name labels from the model configuration
labels = model.config.id2label

# Convert probabilities tensor to a list
probs_list = probabilities[0].tolist()

# Combine class names with their predicted probabilities and sort them
predictions = {labels[i]: probs_list[i] for i in range(len(probs_list))}
sorted_predictions = sorted(predictions.items(), key=lambda item: item[1], reverse=True)

# Print the results
print("Predicted Emotions and Probabilities:")
for emotion, prob in sorted_predictions:
    if prob > 0.1:  # Only display emotions with > 10% probability
        print(f"{emotion}: {prob:.4f}")
