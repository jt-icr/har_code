#!/usr/bin/env python3.5
"""
Pipeline script's steps:
1) Runs muscle program on a set of fasta files, producing *aln outfiles
2) Runs muscle on aln files to make neighbor joining tree *phy outfiles
3) Process *phy files with regex and make one formatted newick style file 
   with all trees for the topd_v3.3.pl tree comparison program
4) Separately run the processed tree file from step 3 with topd_v3.3.pl
!Run this script in the same directory with starting fasta files
Script creator: JP Tomkins, Nov 20, 2015 <jtomkins@icr.org>
"""
from subprocess import call
from os import listdir, system
from re import compile, sub

############################
# 1) Do multiple alignments
############################

#Put fasta files (*.fa extension) in list
gene_files = [file for file in listdir('.') if file.endswith('fa')]

#Run muscle on each gene file, program  info will print to stdout
for gene_file in gene_files:
    fo = gene_file.rsplit('.',1)[0] + '.aln'
    call(['muscle', '-in', gene_file, '-out', fo])

#Print a list of the outfiles
for f in listdir(): 
    if f.endswith('aln'):
        print(f)

##########################################################
# 2) Make neighbor joining trees from multiple alignments
##########################################################

#Put files (*.aln extension) in list
aln_files = [file for file in listdir('.') if file.endswith('aln')]
 
#Run muscle on each gene file, program info will print to stdout
for aln_file in aln_files:
    fo = aln_file.rsplit('.',1)[0] + '.phy'
    call(['muscle', '-maketree','-in', aln_file, '-out', fo,
            '-cluster', 'neighborjoining'])

#Print a list of the outfiles
for f in listdir(): 
    if f.endswith('phy'):
        print(f)        

# 3) Process *phy files with regex and make one formatted file with 
#    all trees for the topd_v3.3.pl program
######################################################################

#Put *.phy files in list
phy_files = [file for file in listdir('.') if file.endswith('phy')]

#Remove chars and make newick style file for topd_v3.3.pl
fo = open('all_trees.nwk', 'w')
regex = compile(r' |:|\.|\de|e-|-|[0-9]|\n')

for phy_file in phy_files:
    fi = open(phy_file, 'r')
    line_title = phy_file.rsplit('.',1)[0]
    data = ''.join([regex.sub('', line) for line in fi])
    fo.write(line_title + '\t' + data + '\n')

#Print outfile
for f in listdir(): 
    if f.startswith('all_'):
        print(f)     

"""
Run the processed *nwk file from step 3 with topd_v3.3.pl
Use: ./topd_v3.3.pl -f all_trees.nwk -out tree_top_out.txt -m all -u all

FYI:
system('./topd_v3.3.pl', '-f', 'all_trees.nwk', '-out', 
       'tree_comp_topd_out.txt', '-m', 'all', '-u', 'all')
       
    gives Perl error: 'Illegal division by zero at ./topd_v3.3.pl line 2623.'

Can remove gene headings from each line with the following one-liner:
"perl -pi -e 's/^har.*\t//g' all_trees.nwk" for other tree comp programs.
"""
