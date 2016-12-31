from janome.tokenizer import Tokenizer
import collections 

t = Tokenizer()
tokens = t.tokenize("エンジニアか美容師の彼女が欲しいエンジニア")
counter = []

for token in tokens:
    partSpeech = token.part_of_speech.split(',')[0]
    if partSpeech == "名詞":
        counter.append(token.surface)
    else:
        pass

counter = collections.Counter(counter)
print(counter.most_common(2))

