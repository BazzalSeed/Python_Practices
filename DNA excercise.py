dna = 'agcttttcattctgactgcaacgggcaatatgtctctgtgtggattaaaaaaagagtgtctgatagcagcttctgaactggttacctgccgtgagtaaattaaaattttattgacttaggtcactaaatactttaaccaatataggcatagcgcacagacagataaaaattacagagtacacaacatccatgaaacgcattagcaccaccattaccaccaccatcaccattaccacaggtaacggtgcgggctgacgcgtacaggaaacacagaaaaaagcccgcacctgacagtgcgggcttttttttcgaccaaaggtaacgaggtaacaaccatgcgagtgttgaagttcggcggtacatcagtggcaaatgcagaacgttttctgcgggttgccgatattctggaaagcaatgccaggcaggggcaggtggccaccgtcctctctgcccccgccaaaatcaccaaccatctggtagcgatgattgaaaaaaccatt'
#1 Dna upper
def dnaUpper(dna):
    D = dna.upper()
    return D

print dnaUpper(dna)

#2 transcription
dna = dnaUpper(dna)

def transcribe(dna):
    mRNA = ''
    for i in dna:
        if i == 'A':
            mRNA = mRNA + 'U'
        elif i == 'C':
            mRNA = mRNA + 'G'
        elif i == 'G':
            mRNA = mRNA + 'C'
        elif i == 'T':
            mRNA = mRNA + 'A'
        else:
            mRNA = mRNA + i
    return mRNA
print transcribe(dna)


#3 find ATG

def findATG(dna):
    for i in range(len(dna)):
        if dna[i:i+3]== 'ATG':
            return i
print findATG(dna)

#4 palindrome
test = 'aaaaaaaaaaaa'

def palindrome(dna):
    rev =''
    for i in dna:
        rev = i + rev
    return rev == dna
print palindrome(test)

#5 Codons

def printCodons(dna):
    for i in range(0,len(dna),3):
        print dna[i:i+3]

printCodons(dna)

#6 count
def CpG(dna):
    t = 0
    for i in range(len(dna)):
        if dna[i:i+1] == 'CG':
            t = t+1
    return t
print CpG(dna)

def CpG2(dna):
    return dna.count('CG')
print CpG(dna)


# 7 hamming

def hamming(dna1,dna2):
    if len(dna1)!=len(dna2):
        return -1
    else:
        t = 0
        n = 0
        for i in dna1:
            if dna[t] !=i:
                n = n+1
            t = t+1
        return n

print hamming(dna,dna+'x')

#8
