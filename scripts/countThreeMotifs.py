import countMotifs as cm
import glob
import re

fasta_files = glob.glob('data/fasta/*.fa')

# Motifs to search for
# S. typhi GATCAG
# E. ferg GCTAAT
# E. coli GGTAAG
motifs = ['GATCAG', 'GCTAAT', 'GGTAAG']

with open('output/motif_counts.csv', 'w') as f:
    f.write('phage,motif,position,strand\n')
    for fasta in fasta_files:
        print(fasta)
        fasta_name = re.sub('\\..*', '', re.sub('.*/', '', fasta))
        print(fasta_name)
        for motif in motifs:
            print(motif)
            hits = cm.searchForMotif(cm.readGenome(fasta), motif)
            for h in hits:
                f.write(str(fasta_name)+','+str(motif)+','+h+'\n')

with open('output/phage_lengths.csv', 'w') as f:
    f.write('phage,genome_length\n')
    for fasta in fasta_files:
        fasta_name = re.sub('\\..*', '', re.sub('.*/', '', fasta))
        fasta_length = len(cm.readGenome(fasta))
        f.write('%s,%d\n' % (fasta_name, fasta_length))
