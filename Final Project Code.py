'''
Joyce Sun
Final Project Code

includes all code i used, including from 'formatting.py'
'''
import math
import os

def weight_at_position(file_name, position):
    '''
    takes file name, position (int) -> dict{}
    traverses all bases at position indicated,
    returns dictionary of weighted scores for each base
    '''
    file = open(file_name, 'r')
    A = 0
    G = 0
    C = 0
    T = 0
    w_A = 0
    w_G = 0
    w_C = 0
    w_T = 0
    nuc_dict = {'A':0, 'G':0, 'C':0, 'T':0} #tabulates which bases are in the same position of different gene seqs. 
    for line in file:
        if line[position] == 'A':
            A += 1
        if line[position] == 'G':
            G += 1
        if line[position] == 'C':
            C += 1
        if line[position] == 'T':
            T += 1
    total = A + G + C + T #tabulates total number of bases
    w_A = A/total #frequency
    w_G = G/total
    w_C = C/total
    w_T = T/total
    if w_A == 0:
        nuc_dict['A'] = w_A
    else:
        nuc_dict['A'] = math.log2(w_A) + 2 
    if w_G == 0:
        nuc_dict['G'] = w_G
    else:
        nuc_dict['G'] = math.log2(w_G) + 2
    if w_C == 0:
        nuc_dict['C'] = w_C
    else:
        nuc_dict['C'] = math.log2(w_C) + 2
    if w_T == 0:
        nuc_dict['T'] = w_T
    else:
        nuc_dict['T'] = math.log2(w_T) + 2
    file.close()
    return nuc_dict

#print(weight_at_position('top10%_nogene.txt', 7))

def total_weights(file_name):
    '''
    file->nested dict{}
    takes a file and runs weight_at_position for each nucleotide position
    outputs a nested dict of the weight scores of nucleotides at each position
    for the genes in the file indicated
    '''
    total_dict = {}
    x = int(input('input sequence length: '))
    for i in range(0,x-1):
        total_dict[i] = weight_at_position(file_name,i)
    return total_dict

#test histogram of weights
#print(total_weights('test.txt'))

def information_by_line(file_name):
    '''
    file->dict
    using weight matrices calculated from weight_at_position within
    total_weights for each line
    '''
    file = open(file_name, 'r')
    total_dict = total_weights(file_name)
    info_score_dict = {}
    line_num=0
    for line in file:
        info_score=0
        for i in range(0,len(line)):
            if line[i] == 'A':
                info_score += total_dict[i]['A']
            if line[i] == 'G':
                info_score += total_dict[i]['G']
            if line[i] == 'C':
                info_score += total_dict[i]['C']
            if line[i] == 'T':
                info_score += total_dict[i]['T']
        info_score_dict[line_num] = round(info_score, 2)
        line_num += 1
    file.close()
    return info_score_dict

#test line information based on weight matrix
#print(information_by_line('bottom10%_nogene.txt'))

def information_of_aligned_sequences(file_name):
    '''
    file->int
    using information_by_line averages info scores
    of an entire file of genes
    '''
    file = open(file_name, 'r')
    info_score_dict = information_by_line(file_name)
    total = 0
    for i in range(0,len(info_score_dict)):
        total += info_score_dict[i]
    avg_info = total/len(info_score_dict)
    return avg_info

#test average line info for a file
#print(information_of_aligned_sequences('test.txt'))

'''
print('Information by line for top 10% of protein expression:')
print(information_by_line('top10%_nogene.txt'))
print('\nAverage for top 10% of protein expression:')
print(information_of_aligned_sequences('top10%_nogene.txt'))

print('\nInformation by line for middle 10% of protein expression: \n')
print(information_by_line('middle10%_nogene.txt'))
print('\nAverage for middle 10% of protein expression:')
print(information_of_aligned_sequences('middle10%_nogene.txt'))

print('\nInformation by line for bottom10% of protein expression: \n')
print(information_by_line('bottom10%_nogene.txt'))
print('\nAverage for bottom 10% of protein expression:')
print(information_of_aligned_sequences('bottom10%_nogene.txt'))
'''

def format_file(file, new_file):
    '''
    file->file
    formats downloaded cavener file into a format readable by our functions
    '''
    f=open(file, 'r')
    nf=open(new_file, 'w')
    mylist = []
    for line in f:
        for char in line:
            if char.isnumeric():
                pass
            elif char.isalpha():
                mylist.append(char)
        for i in range(-6,0):
            nf.write(mylist[i])
        nf.write('\n')
    f.close()
    nf.close()

#format_file('cavener.txt', 'readable_cavener.txt') #formats downloaded cavener.txt file
#predicted_seq('readable_cavener.txt')

def predicted_seq(file_name):
    '''
    file->str
    uses total_weights(file_name) fxn to spit out
    predicted gene sequence based on greatest weight
    '''
    file = open(file_name, 'r')
    positions = total_weights(file_name)
    sorted_positions={}
    seq=''
    for key in positions:
        sorted_bases=sorted(positions[key].items(), key=lambda item: item[1], reverse=True)
        sorted_positions[key]=sorted_bases
    for x in sorted_positions:
        tup_list = sorted_positions[x]
        if tup_list[0][1]>= .5:
            base=tup_list[0][0]
            seq+=base
        else:
            base='-'
            seq+=base
    file.close()
    return seq


print(predicted_seq('-6...-1_top10.txt'))
print('\n')
print(predicted_seq('-6...-1_mid10.txt'))
print('\n')
print(predicted_seq('-6...-1_bottom10.txt'))
print('\n')
print(predicted_seq('readable_cavener.txt'))
