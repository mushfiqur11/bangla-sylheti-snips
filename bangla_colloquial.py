from transformers import AutoModelForPreTraining, AutoTokenizer

banglaTokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglabert")

banglaVocab = banglaTokenizer.get_vocab()

englishTokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

englishVocab = englishTokenizer.get_vocab()

# unified_vocab = banglaVocab.copy()
# for token, token_id in englishVocab.items():
#     if token not in unified_vocab:
#         unified_vocab[token] = max(unified_vocab.values()) + 1

unified_tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglabert", additional_special_tokens=list(englishVocab.keys()))

unified_tokenizer.save_pretrained('unified_tokenizer')