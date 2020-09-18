

from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY") 

connection = Connection(API_KEY)
print("CONNECTOIN", type(connection))

if __name__ == "__main__":

    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]
    embeddings = list(connection.embed_sentences(sentences))
    print(embeddings)

    embedding = connection.embed_sentence("Hello world!!!", model="twitter")
    print(type(embedding)) #> <class 'list>
    print(type(embedding[0])) #> <class 'float'>
    print(len(embedding)) #768
