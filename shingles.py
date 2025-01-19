import binascii
import sys
file_path = 'C:\Voinich\\Pages\\spacy_parsing_f15.txt'
with open(file_path, 'r') as file:
    dep_list = file.read().split('\n')
dict_pairs = {}

# generate list of shingles for source string
def gen_shingle(source):
    shingleLen = 3 # shingle length
    out = []
    for i in range(len(source.split())-(shingleLen-1)): # calculate number of shingles
        out.append(' '.join([x for x in source.split()[i:i+shingleLen]]).encode('utf-8'))
    return out # return list of shingles

# generate list of shingle codes (CRC32) for sh_l list of shingles
def gen_shingle_code (sh_l):
    out = []
    for i in sh_l:
        out.append(binascii.crc32(i))
    return out # return list of shingle codes

# compare 2 sentences (shingle code lists) and return the indexes of the matching shingles
def compare (source1,source2):
    match = []
    for i in range(len(source1)):
        if source1[i] in source2:
            match.append(i)
    return match

sh_list = []
sh_code_list = []
# generate list of shingles and list of shingle codes for all sentences
for i in range (len(dep_list)):
    sh_list.append(gen_shingle(dep_list[i]))
    sh_code_list.append(gen_shingle_code(sh_list[i]))

# generate matrix of matching shingles for each i-j pair of sentences
comp_matrix = []
for i in range(len(sh_list)):
    i_row = []
    for j in range(len(sh_list)):
        if i != j: # do not compare sentence (list of shingles) with itself
            i_row.append(compare(sh_code_list[i],sh_code_list[j]))
    comp_matrix.append(i_row)

# print compare results into file
sys.stdout = open('C:\Voinich\\Pages\\shıngles_f15.txt', 'w')
for i in range(len(comp_matrix)):
    # print("Sentence "+str(i)+"\n------------------")
    for j in range(len(comp_matrix[i])):
        if i!=j and len(comp_matrix[i][j]) != 0:
            for k in comp_matrix[i][j]:
                print(sh_list[i][k])
        # use this block of code to print results in readable format. Block 'if i!=j ...' should be commented
        # print("------Sentence " + str(j) + ':')
        # if i==j:
        #     print('-')
        # else:
        #     if len(comp_matrix[i][j]) == 0:
        #         print("no matches")
        #     else:
        #         # print('\n')
        #         for k in comp_matrix[i][j]: # range(len(comp_matrix[i][j])):
        #             print(sh_list[i][k])
print(comp_matrix)
