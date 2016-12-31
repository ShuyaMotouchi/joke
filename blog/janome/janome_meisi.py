from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize("エンジニアか美容師の彼女が欲しいエンジニア")
  
for token in tokens:
    partSpeech = token.part_of_speech.split(',')[0]
    if partSpeech == "名詞":
        print(token.surface)
    else:
        pass
