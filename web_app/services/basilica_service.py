#web_app_/service/basilica_service.py
from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv() #gets content of the .env file into the enviornment

BASILICA_API_KEY= os.getenv("BASILICA_API_KEY", default="OOPS")

connection = Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ == "__main__":


    embedding = list(connection.embed_sentence("HELLO WORLD"))
    print(embedding) 

    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]


    embeddings = list(connection.embed_sentences(sentences))
    for embed in embeddings: 
        print("----------")
        print(embed)






