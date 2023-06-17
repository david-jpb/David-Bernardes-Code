import random

def generate_dna_strand(length):
    nucleotides = ['A', 'C', 'G', 'T']
    dna_strand = [random.choice(nucleotides) for _ in range(length)]
    return dna_strand

def generate_complement(dna_strand):
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement_sequence = [complement[nucleotide] for nucleotide in dna_strand]
    return ''.join(complement_sequence)

dna_length = int(input("Enter the length of the DNA strand: "))
dna_strand = generate_dna_strand(dna_length)
complement_sequence = generate_complement(dna_strand)

print("DNA strand:", ''.join(dna_strand))
print("Complement sequence:", complement_sequence)
