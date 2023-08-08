# SMARTHIRE.Al

![SmartHireAI](https://github.com/Shreyanthds/SMARTHIRE.Al/assets/115062429/2b07ed46-cf02-4637-926a-740db755e92c)


**Streamlit application for a project called "SmartHire.AI."**

It helps candidates assess how well their resume matches a given job description using natural language processing (NLP) techniques. The application takes the job description as input and allows users to upload their resume in PDF format. It then calculates the similarity between the job description and the resume and provides an overview and suitability evaluation based on the similarity score.

The main components of the code are as follows:

**Importing Libraries:**

The code begins by importing required libraries such as
1. Streamlit,
2. PyPDF2,
3. spaCy,
4. NLTK,
5. CountVectorizer,
6. cosine_similarity.


**Data Preparation:**

The NLTK data path is set to the location of NLTK data files to support the use of stopwords.
The spaCy model for English language processing ('en_core_web_sm') is loaded, and the set of English stopwords from NLTK is also loaded.
Text Preprocessing:

The code defines a function 'preprocess_text' that takes a text input and performs the following steps:
1. Converts the text to lowercase
2. Tokenizes the text using spaCy
3. Removes stopwords and non-alphabetic tokens
4. Lemmatizes the remaining tokens
5. Returns the preprocessed text as a string.
6. Similarity Calculation:




<img width="612" alt="NLP" src="https://github.com/Shreyanthds/SMARTHIRE.Al/assets/115062429/a66aefa6-a33b-47db-b4e0-6dfaabda99ee">



The results, including the similarity score, the overview message, and the suitability evaluation, are displayed on the web application.
The SmartHire.AI project aims to assist job seekers in improving their resumes to match job descriptions more effectively and increase their chances of being considered for suitable positions. By leveraging NLP and cosine similarity, the application provides valuable insights to candidates on how they can enhance their resumes to align better with job requirements.
