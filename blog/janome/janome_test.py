from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize("エンジニアか美容師の彼女が欲しいエンジニア")
  
for token in tokens:
    print(token)
