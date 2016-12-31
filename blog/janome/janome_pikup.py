from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize("エンジニアか美容師の彼女が欲しいエンジニア")
  
for token in tokens:
    print(token.surface, '\t',)                  # 表層形
    print(token.part_of_speech.split(',')[0],)   # 品詞
    print(token.part_of_speech.split(',')[1],)  # 品詞細分類1
    print(token.part_of_speech.split(',')[2],)   # 品詞細分類2
    print(token.part_of_speech.split(',')[3],)   # 品詞細分類3
    print(token.infl_type,)                      # 活用型
    print(token.infl_form,)                      # 活用形
    print(token.base_form,)                      # 原形
    print(token.reading,)                        # 読み
    print(token.phonetic,)                       # 発音
    print(token.node_type,) 
