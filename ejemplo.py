from Bio.Seq import Seq,MutableSeq
from Bio.Alphabet import generic_dna,generic_rna,IUPAC

sequence = Seq('AGTACACTGGT',generic_dna)
print(sequence)
print(sequence.alphabet)
print(sequence.complement())
print(sequence.reverse_complement())
sequence = Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG',generic_dna)
print(sequence.translate())
print(sequence.translate(to_stop=True))

"""
print("Pass DAN to RNA")
rna = sequence.transcribe()
print(rna)
print(rna.back_transcribe())

print("Translate")
rna1 = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG",generic_rna)
print(rna1.translate())

print("Sequence Mutable")
mutable = MutableSeq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG",IUPAC.unambiguous_dna)
print(mutable)
mutable[3]="T"
print(mutable)
"""
