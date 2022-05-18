import os

def info_frame(file, newfile):
    readfile= open(file, "r")
    f=open(newfile, "w")
    for line in readfile:
        i=0
        flag=0
        while i<len(line):
            if line[i]=='	':
                flag=1
                f.write(line[:i]) #gene name
                f.write('\n') #new line
                f.write(line[i+991:i+1000]) #-10 before ATG
                f.write(line[i+1004:i+1014]) #+10 after ATG
                f.write('\n') #new line
                #f.write(line[i+866:i+1000]) #-135 and ATG into 5'UTR
                #f.write('\n') #new line
                #f.write(line[i+1001:i+2073]) #ATG +1069
                #f.write('\n') #new line
                #f.write(line[i+994:i+1000]) #-6...-1
                #f.write('\n') #new line
            i+=1
    readfile.close()
    f.close()

info_frame('top.txt', "top10%.txt")
info_frame('bottom.txt', "bottom10%.txt")
info_frame('mid.txt', "middle10%.txt")

#middle centered around 50% protein expression probability, 45-55%
#positions 10 nucleotides before (-10 to -1) ATG and 10 nucleotides after ATG (0 to 9)




