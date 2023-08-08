#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 12:11:06 2023

@author: shreyanthhg
"""

import streamlit as st
import PyPDF2
import spacy
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set the data path for NLTK
nltk.data.path.append("/path/to/nltk_data")

# Load the spaCy model and set up the NLTK stop words
nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenize, remove stop words, and lemmatize the text
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.text.isalpha() and token.text not in stop_words]
    return ' '.join(tokens)

def calculate_similarity(job_desc, resume_text):
    # Preprocess the job description and resume text
    job_desc_processed = preprocess_text(job_desc)
    resume_text_processed = preprocess_text(resume_text)

    # Calculate similarity using cosine similarity
    vectorizer = CountVectorizer().fit_transform([job_desc_processed, resume_text_processed])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors)[0][1]

    return similarity * 100

def generate_resume_overview(similarity):
    # Generate an overview message based on the similarity score
    if similarity >= 100:
        return "Your resume is a perfect match for the job description!"
    else:
        missing_percentage = 100 - similarity
        return f"Your resume is {similarity:.2f}% similar to the job description. Consider adding more relevant experiences or skills to achieve a 100% match. You are missing approximately {missing_percentage:.2f}% of the required qualifications."

def is_candidate_suitable(similarity, threshold=70):
    # Determine whether the candidate is suitable based on the similarity score
    return similarity >= threshold


def main():
    st.title("SmartHire.AI")
    
    st.image("/Users/shreyanthhg/Desktop/AI Resume/SmartHireAI.png")

    # Job description input
    job_desc = st.text_area("Enter the job description:")

    # Resume file upload
    uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

    if job_desc and uploaded_file:
        # Read the uploaded resume PDF using PdfReader
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # Calculate similarity
        similarity = calculate_similarity(job_desc, resume_text)

        # Generate resume overview
        overview = generate_resume_overview(similarity)

        # Check suitability
        is_suitable = is_candidate_suitable(similarity)

        # Display results
        st.write(f"Resume Similarity: {similarity:.2f}%")
        st.write(overview)
        if is_suitable:
            st.write("You are best suited for this job!")
        else:
            st.write("You may need to improve your resume to be a strong candidate for this job.")


if __name__ == "__main__":
    main()
