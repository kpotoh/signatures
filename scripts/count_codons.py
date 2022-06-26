# USAGE: python3 count_codons.py HUMAN_GENOME OUT_COUNTS_JSON

import json
import os
import sys
from collections import defaultdict

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

PATH_TO_GENOME = "./data/external/human_genome/GCF_000001405.25_GRCh37.p13_genomic.fna"
PATH_TO_JSON_OUT = "./data/interim/codon_counts_GRCh37.json"

NUCL_SET = set("ACGTacgt")


def is_appropriate_codon(codon: str) -> bool:
    return len(set(codon).difference(NUCL_SET)) == 0


def main(path_th_genome, path_to_out):
    codon_counts = defaultdict(int)
    fasta = SeqIO.parse(path_th_genome, "fasta")
    rec: SeqRecord = None
    for rec in fasta:
        print("Processing...", rec.description, file=sys.stderr)
        seq = str(rec.seq)
        # iterate over codons with window=1
        for i in range(len(seq) - 2):
            codon = seq[i: i + 3]
            if is_appropriate_codon(codon):
                codon_counts[codon] += 1

    print(codon_counts, file=sys.stderr)
    with open(path_to_out, "w") as fout:
        json.dump(codon_counts, fout)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Pass 2 arguments: HUMAN_GENOME and OUT_COUNTS_JSON")
    if not os.path.exists(sys.argv[1]):
        raise ValueError(f"Path ({sys.argv[1]}) doesn't exist")
    main(sys.argv[1], sys.argv[2])
