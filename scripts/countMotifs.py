from Bio import SeqIO
import pandas as pd
import argparse

alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def get_options():
    parser = argparse.ArgumentParser(description='Count motifs in a fasta file.',
                                                    prog='countMotifs')
    parser.add_argument('--fasta', help='Input fasta file', required=True)
    parser.add_argument('--motif', help='Motif to search for', required=True)
    return parser.parse_args()


def reverseComplement(seq):
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq)
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases


def readGenome(fasta_file):
    '''read in a fasta file'''
    sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, 'fasta'))
    if len(sequences)!=1:
        return
    if len(sequences)==1:
        for seq in sequences:
            return(str(sequences[seq].seq).upper()) # make sure upper

def motifLocations(sequence, motif, reverse=False):
    '''Returns motif start positions in a sequence.
    Args:
        sequence
            the sequence to search within
        motif
            the motif to search for
        reverse (optional)
            whether the reverse strand is desired
    Output:
        list of start locations of hits (+1 so we are in 1-indexed)
    '''
    if reverse==False:
        return([i+1 for i in range(len(sequence)-len(motif)) if sequence[i:i+len(motif)]==motif ])
    elif reverse==True:
        return([i+1 for i in range(len(sequence)-len(motif)) if reverseComplement(sequence[i:i+len(motif)])==motif ])

def searchForMotif(sequence, search_motif):
    '''just combines forward and reverse hits'''
    forward_hits = motifLocations(sequence, search_motif)
    reverse_hits = motifLocations(sequence, search_motif, reverse=True)
    total_hits = [str(x)+',+' for x in forward_hits] + [str(x)+',-' for x in reverse_hits]
    #for hit in total_hits:
    return(total_hits)


def main():
    args = get_options()
    seq = readGenome(args.fasta)
    motif = args.motif.upper()
    print(searchForMotif(seq, motif))

if __name__=="__main__":
    main()
