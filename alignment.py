from Bio.Seq import Seq
from Bio import pairwise2
from Bio.Alphabet import generic_dna,generic_rna,IUPAC

seq1 = Seq("ATGCT",generic_dna)
seq2 = Seq("ATT",generic_dna)

aligment = pairwise2.align.globalxx(seq1,seq2)

print(pairwise2.format_alignment(*aligment[0]))
