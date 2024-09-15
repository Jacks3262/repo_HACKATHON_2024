# repo_HACKATHON_2024
Official repository of the Datacoders team, where analyses were conducted for Capital One's organization in the 2024 HACKATHON.

## Members of DataCoders
* Luis Maximiliano López Ramírez - A00833321
* Dilan González Castañeda - A00831905
* Rogelio Lizárraga Escobar - A01742161
* Adrian Pineda Sánxhez - A00834710

# Proyect with Capital One

The issue of fraud in transactions is a growing challenge for businesses and consumers worldwide. As digital transactions expand and diversify, new opportunities arise for fraudsters seeking to exploit payment systems. Frauds can take various forms, from credit card misuse to identity theft and transaction manipulation on online platforms. These incidents not only cause significant financial losses but also erode customer trust and damage the reputation of the affected companies.

# Solution

To address the growing issue of fraud in transactions, an effective solution has been the implementation of machine learning tools and the use of TensorFlow for neural networks, which efficiently classify fraudulent transactions. These technologies analyze large volumes of data in real-time, identifying suspicious patterns and anomalies that could indicate fraud. Through supervised and unsupervised learning, machine learning models are trained with historical transaction data, allowing them to detect atypical behaviors with high accuracy. TensorFlow, with its ability to develop complex neural networks, enhances automated fraud detection through classification models that continuously learn and adapt to new fraudulent tactics.

# File's distribution

## Datasets

Here are the datasets generated from the scripts and the original dataset.
* **fraud.csv**
* **heybanco.csv**
## Scripts

Contains the .py and .ipynb codes for solving the stated problem.

* **Fraud.py:** Performs the transformation of the original dataset to create columns of interest, generating **fraud.csv.**
* **Modelos_Convencionales.ipynb:** Based on **fraud.csv**, conventional Machine Learning models are generated for the detection of fraudulent transactions.
* **Modelos_Hackathon.ipynb:** Based on **fraud.csv**, several neural networks are generated with TensorFlow for the detection of fraudulent transactions, obtaining the best prediction model here.
* **crew_ai_csv_decode.py:** Python code that uses LLM to generate reports and insights of interest from fraud.csv.

## Demonstrations

## flask-react
There was an attempt to create a backend api in Flask and connect it directly with a frontend developed in React, with the purpose of showing the most relevant information we gathered in our analysis.

Contains the demo video of some tests of the fraudulent transaction prediction model, as well as the presentation used for the Capital One presentation.
* **Final presentation.pdf**
* **Video_Hackathon_2.mp4**
