#9.28  new string; replace
dna='atcgggatcgaatcggatcgtaaacgtagc'
#1 built-in method
print dna.replace('t','u')

def dnatoRna(dna):
    rna = ''
    for i in dna:
        if i == 't':
           rna = rna + 'u'
        else:
           rna = rna + i
    return rna
    
def compliment(dna):
    compliment = ''
    for i in dna:
        if i == 'a':
           compliment = compliment + 't'
        elif i == 'c':
            compliment = compliment + 't'
        elif i == 'g':
             compliment = compliment + 't'
        elif i == 't':
             compliment = compliment + 'g'
    return compliment
print compliment(dna)

#reverese dna
def reverse(dna):
    revdna = ''
    for i in dna:
        rev = i + rev
    return rev
       
           
