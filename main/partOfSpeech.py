from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk.tree import Tree


text = """Full stack software developer Nithin Reddy Ganji has expertise in technologies spanning 
          from web development to microservices and distributed systems.
           He also works on DevOps tools like Ansible and Jenkins. Nithin Reddy Ganji"""

sentences = sent_tokenize(text)
persons = []
currentPerson=' '
string1 = "some1"
string2 = "some2"
print(string1 +' '+ string2)
for sentence in sentences:
    words = word_tokenize(sentence)
    partOfSpeeches = pos_tag(words)
    taggedWords = ne_chunk(partOfSpeeches)
    for taggedWord in taggedWords:
        
        if type(taggedWord) == Tree:
            if(getattr(taggedWord,'_label') == 'PERSON'):
                print(taggedWord)
                if(currentPerson!=' '):
                    print(currentPerson)
                    for k in taggedWord:
                        currentPerson = currentPerson + ' '+k[0]
                    print("In here") 
                else:
                    print("In here xx") 
                    currentPerson = currentPerson.join(k[0] for k in taggedWord)
                    print(currentPerson)
            else:
                if(currentPerson!=' '):
                    persons.append(currentPerson) 
                    currentPerson = ' '        

if(currentPerson!=' '):
    persons.append(currentPerson) 
    currentPerson = ' '        

print(persons)                
