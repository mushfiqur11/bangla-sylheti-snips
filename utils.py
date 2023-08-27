import pymongo
import json
from transformers import BertTokenizer
from transformers import AutoModelForPreTraining, AutoTokenizer
from normalizer import normalize


def get_db(mongo_username, mongo_password, db_name='NLU'):
    client = pymongo.MongoClient(f'mongodb+srv://{mongo_username}:{mongo_password}@cluster0.vwjnph6.mongodb.net/?retryWrites=true&w=majority')
    db = client[db_name]
    return db

def get_all_documents(collection):
    documents = []
    for document in collection.find():
        documents.append(document)
    return documents

def convert_to_bio_format(data):
    # Split the text into words
    words = data['text'].split()

    # Initialize the slots list with 'O'
    slots_bio = ['O'] * len(words)

    # For each slot name and value, update the slots_bio list
    for slot_name, slot_value in data['slots'].items():
        if slot_value:  # if the slot value is not an empty string
            value_words = slot_value.split()
            start_idx = None

            # Try to find the start of the slot value in the words list
            for i in range(len(words) - len(value_words) + 1):
                if words[i:i+len(value_words)] == value_words:
                    start_idx = i
                    break

            if start_idx is not None:
                # Set the beginning slot
                slots_bio[start_idx] = f'B-{slot_name}'

                # Set the inside slots
                for j in range(1, len(value_words)):
                    slots_bio[start_idx + j] = f'I-{slot_name}'

    return {
        'text': data['text'],
        'slots': slots_bio
    }

tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglabert")

def convert_to_bio_format_bengali(data):
    sentence = data['text'].strip('<pad>').strip('</s>').strip(' ').strip('\n')
    sentence = normalize(sentence)
    # Tokenize the text into words
    words = tokenizer.tokenize(sentence)
    print(words)
    # Initialize the slots list with 'O'
    slots_bio = ['O'] * len(words)

    # For each slot name and value, update the slots_bio list
    for slot_name, slot_value in data['slots'].items():
        if slot_value:  # if the slot value is not an empty string
            slot_value_normalized = normalize(slot_value)
            value_words = tokenizer.tokenize(slot_value_normalized)
            start_idx = None

            # Try to find the start of the slot value in the words list
            for i in range(len(words) - len(value_words) + 1):
                if words[i:i+len(value_words)] == value_words:
                    start_idx = i
                    break

            if start_idx is not None:
                # Set the beginning slot
                slots_bio[start_idx] = f'B-{slot_name}'

                # Set the inside slots
                for j in range(1, len(value_words)):
                    slots_bio[start_idx + j] = f'I-{slot_name}'

    return {
        'text': sentence,
        'slots': slots_bio
    }



