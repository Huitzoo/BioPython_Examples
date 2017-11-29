from Bio import SeqIO
lista = []
#SHow a fasta file, you have to said the format to document reading
for seq_record in SeqIO.parse('genbank.gbk','genbank'):
    print(seq_record.id)
    lista.append(seq_record.seq) #It show us a little representation.
    print(len(seq_record))
print(lista)
