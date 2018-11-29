from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk.tree import Tree


text = """Nithin Reddy Ganji is a Full stack software developer and has expertise in technologies spanning 
          from web development to microservices and distributed systems.
           He also works on DevOps tools like Ansible and Jenkins."""

sentences = sent_tokenize(text)

for sentence in sentences:
    words = word_tokenize(sentence)
    partOfSpeeches = pos_tag(words)
    taggedWords = ne_chunk(partOfSpeeches)
    for taggedWord in taggedWords:
        if type(taggedWord) == Tree:
            print('label is: {0}'.format(taggedWord))
            print(taggedWord.label(), ' '.join(k[0] for k in taggedWord))
