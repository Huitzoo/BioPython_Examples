from Bio import SeqIO,pairwise2
from Bio.pairwise2 import format_alignment
#SHow a fasta file, you have to said the format to document reading
"""
for seq_record in SeqIO.parse('genbank.fasta','fasta'):
    print(seq_record.id)
    print(seq_record.seq.translate()) #It show us a little representation.
    print(len(seq_record))"""

count = SeqIO.convert("genbank.gbk", "genbank", "genbank.fasta", "fasta")
print("Converted %i records" % count)

lista = []
#SHow a fasta file, you have to said the format to document reading
for seq_record in SeqIO.parse('genbank.fasta','fasta'):
    print(seq_record.id)
    lista.append(seq_record.seq) #It show us a little representation.
    print(len(seq_record))

aligment = pairwise2.align.globalxx(lista[0],lista[1])

print(format_alignment(*aligment[0]))
