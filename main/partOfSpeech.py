from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk.tree import Tree


text = """Nithin Reddy Ganji is a Full stack software developer. He has expertise in technologies spanning 
          from web development to microservices and distributed systems.
          also works on DevOps tools like Ansible and Jenkins. """

sentences = sent_tokenize(text)
persons = []
currentPerson=''

for sentence in sentences:
    words = word_tokenize(sentence)
    partOfSpeeches = pos_tag(words)
    taggedWords = ne_chunk(partOfSpeeches)
    for taggedWord in taggedWords:
    
        if type(taggedWord) == Tree:
            print(taggedWord)
            if(getattr(taggedWord,'_label') == 'PERSON'):
                for k in taggedWord:
                        currentPerson = currentPerson + ' '+k[0]
            else:
                if(currentPerson!=''):
                    persons.append(currentPerson) 
                    currentPerson = ''  
                        
        else:
            if(currentPerson!=''):
                persons.append(currentPerson) 
                currentPerson = ''  
                

if(currentPerson!=''):
    print(currentPerson)
    persons.append(currentPerson) 
    currentPerson = ''        

print(persons)                
