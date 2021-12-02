import spacy

text = """Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets."""

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
# Make tokens for the initial text and removing non relevant words like (but, as, then)
token_list = [token for token in doc if not token.is_stop]
lemmas = [f"Token: {token}, lemma: {token.lemma_}" for token in token_list]

print(token_list[1].vector)
