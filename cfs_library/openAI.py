import openai
import os
import json
import jsonlines

# OpenAI authorization
openai.organization = "org-MVRMhL527YpFJrqDkAP9ivu5"
openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.Engine.list()
# response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)

# This function converts a text file into a jsonlines file,
# using the "###" tag as the split indicator.
def textToJsonlines(filename):
    
    textFile = filename + ".txt"
    jsonlFile = filename + ".jsonl"

    # Read text from file
    f = open(textFile, "r")
    
    # This splits the text in the file into a list of text blocks and removes surrounding white space
    documents = f.read().split("###")
    for document in documents:
        document = document.strip()

    # Write documents to jsonlines file in current directory
    with jsonlines.open(jsonlFile, mode='w') as writer:
        for document in documents:
            writer.write({"text": document.strip()})

# This function returns scores from OpenAI API given input question
def apiScore(inputQuestion):

    # Send semantic search query to OpenAI API using Babbage engine
    response = openai.Engine("babbage").search(
        search_model="babbage", 
        query=inputQuestion, 
        max_rerank=5,
        file="file-THEa0jeIEul23nFUj1L8nlVu"
    )

    return response


# ========== MAIN PROGRAM ==========

# Create Jsonlines file and upload to OpenAI
# textToJsonlines("cfs_library")
# openai.File.create(file=open("cfs_library.jsonl"), purpose="search")

# Get response 
question = "What are the different DNA typing methods?"
answer = apiScore(question)

print(answer)