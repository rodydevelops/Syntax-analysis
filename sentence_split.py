list_sent = []
file_path = 'C:\Voinich\\Pages\\f15.txt'

with open(file_path, 'r') as file:
    file_content = file.read().split('\n') # get list of paragraphs from file

from wtpsplit import SaT

file = open('C:\Voinich\\Pages\\sent_split_f15.txt','a+')
sat = SaT("sat-3l-sm")

for paragraph in file_content:
    st = sat.split(paragraph) # split paragraph from file into sentences
    print(*st, sep='\n',file=file) # print sentences as separate lines into file
file.close()