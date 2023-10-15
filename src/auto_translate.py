import pandas as pd
import csv
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize # pip install git+https://github.com/csebuetnlp/normalizer


model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_en_bn")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_en_bn", use_fast=True)


def translate_text(input_sentence):
    input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
    generated_tokens = model.generate(input_ids)
    return tokenizer.batch_decode(generated_tokens)[0]