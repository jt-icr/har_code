#!/usr/bin/env python3.5
"""
Parses the Multiz Alignments & Conservation web output copied and pasted into
a text file from the UCSC genome browser for the taxon listed below (outfile=fasta) 
J.P. Tomkins <jtomkins@icr.org> Oct 15, 2015
"""
import sys

args = sys.argv[1:]
if len(args) != 1 :
    print("Error!  Argument needed: input file name")
    sys.exit()
    
filename = args[0]
fi = open(filename, 'r')
fo = open(filename + '.fa', 'w')

#Make lists for each taxa to hold sequences
human     = []
chimp     = []
gorilla   = []
orangutan = []
rhesus    = []
dog       = []
elephant  = []
chicken   = []
mouse     = []
cow       = []

for line in fi:
    line = line.replace('B ','') #Strip letters B/D and leading whitespace
    line = line.replace('D ','')
    line = line.lstrip()
    linestart = ('Hu','Ch','Go','Or','Rh','Do','El','Mo','Co') #Tuple for startswith()
    if line.startswith(linestart):
        cols = line.replace('-','').rstrip('\n').split(' ') #Remove '-' & make list
        while '' in cols:              #Remove empty items from cols list
            cols.remove('')            
        if cols[0] == 'Human':         #Put sequences in proper taxa list
            human.append(cols[1])
        elif cols[0] == 'Chimp':
            chimp.append(cols[1])
        elif cols[0] == 'Gorilla':
            gorilla.append(cols[1])
        elif cols[0] == 'Orangutan':
            orangutan.append(cols[1])
        elif cols[0] == 'Rhesus':
            rhesus.append(cols[1])
        elif cols[0] == 'Dog':
            dog.append(cols[1])
        elif cols[0] == 'Elephant':
            elephant.append(cols[1])
        elif cols[0] == 'Chicken':
            chicken.append(cols[1])
        elif cols[0] == 'Mouse':
            mouse.append(cols[1])
        elif cols[0] == 'Cow':
            cow.append(cols[1])

#Concatenate and print sequences from each list in fasta format    
def seq(seqlist):
    return ''.join(seqlist).upper() + "\n"

fo.write(">Human\n"     + seq(human)
        +">Chimp\n"     + seq(chimp)
        +">Gorilla\n"   + seq(gorilla)
        +">Orangutan\n" + seq(orangutan)
        +">Rhesus\n"    + seq(rhesus)
        +">Dog\n"       + seq(dog)
        +">Elephant\n"  + seq(elephant)
        +">Chicken\n"   + seq(chicken)
        +">Mouse\n"     + seq(mouse)
        +">Cow\n"       + seq(cow)
        )

fi.close()
fo.close()

#Check the file
with open(filename + ".fa", 'r') as fi:
     print(fi.read())
sys.exit()

"""Example input file (har8 aln)...

Alignment block 1 of 2 in window, 39224504 - 39224727, 224 bps 
B D      Human  ggaaaggtggaaaaaag-ttagatatacaagc---aagaaaaagtgagttattgattttattgactggtc
B D      Chimp  ggaaaggtagagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D    Gorilla  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D  Orangutan  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D     Gibbon  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D     Rhesus  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D      Mouse  ggaaaggtgggcaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgaccggtc
B D        Cow  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D        Dog  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D   Elephant  ggaaaggtggagaaaag-ttagatatataagc---aagaaaaagtgagttattgattttattgactggtc
B D    Chicken  agaaaggtggagaaaag-ttagatatataagc---aagaaaaggtgagttattgattttattgactggtc

         Human  tgttaacttctgacattgcaatgaagtcttatttatttgtatacggaagactcaattacatagatacata
         Chimp  tgttaacttctgacattgcaataaagtcttatttatttgtatacggaagactcaattacatagatacata
       Gorilla  tgttaacttctgacattgcaataaagtcttatttatttgtatacggaagactcaattacatagatacata
     Orangutan  tgttaacttctgacattgcaataaagtcttatttatttgtatacagaagactcaattacatagatacata
        Gibbon  tgttaacttctgacattgcaataaagtcttatttatttgtatacggaagactcaattacatagatacata
        Rhesus  tgttaacttctgacattgcaataaagtcttatttatttgtatacggaagactcaattacatagatacata
         Mouse  tgttaacttctgacattgcaataaagtcttatttatttgtatacagaagactcaattacatagatacata
           Cow  tgttaacttctgacattgcaataaagtcttatttatttgtatacagaagactcaattacatagatacata
           Dog  tgttaacttctgacattgcaataaagtcttatttatttgtatacagaagactcaattacatagatacata
      Elephant  tgttaacttctgacattgcaataaagtcttatttatttgtatacagaagactcaattacatagatacata
       Chicken  tgttaacttctgacattgcaataaagccttatttatttgtatacagaagactcaattacatagatacata

         Human  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agacctggaatt
         Chimp  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agacctggaatt
       Gorilla  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agacctggaatt
     Orangutan  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatac-----agagctggaatt
        Gibbon  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agacctggaatt
        Rhesus  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agacctggaatt
         Mouse  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatac-----agagttggaatt
           Cow  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agagctgggatt
           Dog  tcattttaacaactgggttatttacaggagaattgctgcttcataaataatat-----agacctggggtt
      Elephant  tcattttaacaactgggttatttacaggagaattgcagcttcataaataatat-----agacctggaatt
       Chicken  tcattttaacaactgggttatttacagcagaattgcagcttcataaataatac-----agtcctg-aatt

         Human  tttcaagctgatgtttatccatt
         Chimp  tctcaagctgatgtttatccatt
       Gorilla  tctcaagctgatgtttatccatt
     Orangutan  tctcaagctgatgtttatccatt
        Gibbon  tctcaagctgatgtttatccact
        Rhesus  tctcaaactgatgtttatccatt
         Mouse  tctcaagctgatgtttatccatt
           Cow  tctcaagctgatgtttatccatt
           Dog  tctcgagctgatgtttatccatt
      Elephant  tctcaagctgatgtttatccatt
       Chicken  tctcaagctgatgtttatccatt

Alignment block 2 of 2 in window, 39224728 - 39224736, 9 bps 
B D      Human  gttacc--taa
B D      Chimp  gttacc--taa
B D    Gorilla  gttacc--taa
B D  Orangutan  gttatc--taa
B D     Gibbon  gttacc--taa
B D     Rhesus  gttacc--taa
B D      Mouse  gttacc--taa
B D        Cow  gttgcc--tag
B D        Dog  gttacc--taa
B D   Elephant  gttagc--taa
B D    Chicken  gttaccattta
"""

        
        

