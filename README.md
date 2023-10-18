# For my impACT 2023 presentation

## Demo #1 - Zero Shot Classification - ChatGPT
Generally speaking, to train and use a machine learning model, you need relevant labeled data. With Zero Shot Learning we try to solve problems the models have never explicitly seen before. LLMs are generally pretty good at Zero Shot Classification and I find this one of their most useful attributes. #TODO add comment about work relevance

### An Example
```
- Below is a list of 100 professions. The professions are separated by commas and are under the header, DATA.
- Please classify each profession as either “white collar” or “blue collar” or “unknown”. If you are unsure on a profession’s classification, respond with “unknown”. 
- Do not respond with any additional commentary or information. 
- Put your responses in a numbered list from 1 to 100

DATA
teacher, accountant, doctor, engineer, lawyyer, nurrse, electrician, police officer, firefighter, pharmacist, pilot, realetate agent, plumberr, contractor, journalistt, actor, waitress, gardener, surgeon, electrician, physician, psychologist, nuclear physicist, chemist, cok, electritian, lumberjack, garbage man, mechanic, politician, farnmer, dancer, salesman, poet, janitor, chef, masseuse, scientist, politician, veternarian, accountant, engineer, nurse, realtor, pharmacist, eletrcian, police officer, firefighter, piolt, teacher, contractor, actor, nuclear physicist, chemist, electrician, lawyer, surgeon, physicin, phycologist, electrician, garbage man, mechanic, politician, farmer, dancer, salesman, poet, janitor, chef, massuase, scientist, politician, veterinarian, accountant, engineer, nurse, realtor, pharmacist, pilot, teacher, contractor, artist, nucar physcist, chemist, electrician, lawyer, surgon, physician, psychologist, electrician, garbage man, mechanic, politician, farmer, dancer, salesman, poet, janitor, chef, masuase
```

### Another Example
```
Below are a list of terms extracted from engineering reports. 

First, can you determine 4 classes that accurately describe all of the terms?
Second, can you classify each term as one of the classes you determined?

Terms
1) prosthetic limbs
2) insulin
3) needles
4) human growth hormone (HGH)
5) cardboard
6) labels
7) fire hydrants
8) water fille syringes
9) poultry vaccines
10) surgical silk sutures
11) insulin glargine (Basaglar)
12) vitamin B
13) aspirin
14) glass tubes
15) tongue depressors
```
- For a smaller LLM, like Facebook's Llama2, I would recommend splitting this into two prompts. First: identify the classes, second: classify the terms.


## Demo #2 - Learn a new topic - ChatGPT
ChatGPT is a great study buddy. Let's use ChatGPT to Learn about FHIR, Fast Healthcare Interoperability Resources.
```
I need assistance summarizing the various Procedure and Procedure related resources from FHIR HL7. For each resource I need to know what these contain and what their intended use is. Please provide reference links for each resource.
```

```
Can you describe how these resources are interrelated and how they link together?
```

```
How do these resources relate to the Encounter resource?
```

```
What's the difference between an Encounter and an Observation?
```

```
Can you generate code to query the Azure managed FHIR service for a particular person's Procedure resources?
```

ChatGPT can also be very useful as you prepare for and apply to new jobs. Use ChatGPT to generate practice interview questions, then use ChatGPT to grade your responses.

```
What are some typical data science interview questions for a junior data scientist at an insurance company?
```

```
Explain the difference between supervised and unsupervised learning.
```

```
What are 10 common interview questions for a new people manager?
```

```
I am preparing for an interview. Can you critque my response to the following interview question? Highlight what I did well and what I could have done better. 
```

## Demo #3 - The art of improving a prompt - Llama2

I have unstructured medical text, from a doctor's note, and I want to try to use an LLM  to ask life insurance application questions. This example is intentionally based off of using Faecbook's open source LLM Llama2, a worse performing model compared to ChatGPT. These smaller, self hosted, models are more likely to be what small and mid-size enterprises are able to work with internally. 

### Prompt V1
```
You are a trustworthy life insurance agent, recetnly you have recieved the following information from a life insurance applicant. You need to use this applicant's data to answer the following application questions. Please answer each question individually.

{applicant's data here}

1) Do you have a history of heart issues? Choose one of. Yes currently being treated, not in the last 5 years, or never?
2) Do you have a history of anxiety, depression or other psychological issues? Yes currently being treated, not in the last 5 years, or never?
3) Did your mother or father die from or was diagnosed with cancer before the age of 55?
```

### Prompt V2
```
You are evaluating a life insurance applicant. Below is the applicant's information. Answer the question below based on the provided information.

{applicant's data here}

1) Do you have a history of heart issues? Choose one of. Yes currently being treated, not in the last 5 years, or never?
```
- Shorter more concise instructions.
- Fewer questions at a time.

### Prompt V3
```
You are evaluating a life insurance applicant. Below is the applicant's data. Answer the question below based on the provided information.
- Do not hallucinate. 
- Encase your response in three back ticks, ```.
- If you cannot answer the question or are unsure, reply with "unsure"

DATA
{applicant's data}

QUESTION
Have you ever had heart issues?
```
- Increasingly explicit directions.
- Annotating DATA, QUESTION
- Further break down of the question.
