import spacy

file_path = 'C:\Voinich\\Pages\\sent_split_f15.txt'
with open(file_path, 'r') as file:
    st = file.read().split('\n') # get list of sentences from file


nlp = spacy.load('it_core_news_sm')
dep_list = []
file = open('C:\Voinich\\Pages\\spacy_parsing_f15.txt', 'a+')
for sent in st:
    struct_in_sent = []
    doc = nlp(sent) # get sentence syntax structure
    for token in doc:
        struct_in_sent.append(str(token.dep_)) # add all dependencies (tokens) into list
    dep_list.append(struct_in_sent)
# print all sentence structures into file
for i in dep_list:
    print(*i, file=file)
file.close()
