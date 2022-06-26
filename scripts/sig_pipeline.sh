# USAGE: bash sig_pipeline.sh
# Modify arguments directly in this file below (will be fixed in future)

MUTSPEC192="data/sars-cov-2_192.csv"
MUTSPEC96="data/sars-cov-2_96.tsv"
SIGDIR="data/processed/sars-cov-2"

HUMANGENOME="data/external/human_genome/GCF_000001405.25_GRCh37.p13_genomic.fna"
HUMANCOUNTS="data/codon_counts_GRCh37.json"


# 1 calculate trinucleotide counts of human genome
if [ ! -e $HUMANCOUNTS ]; then
    python3 scripts/count_codons.py $HUMANGENOME $HUMANCOUNTS
    echo "Human trinucleotide counts extracted"
else
    echo "Using precalculated human trinucleotide counts"
fi

if [ ! -e $HUMANCOUNTS ]; then
    echo "Error! File '$HUMANCOUNTS' not found!"
    exit 0
fi

# 2 Convert 192-component mutational spectra to 96-component DISCRETE format
python3 scripts/collapse_mutspec.py --inp $MUTSPEC192 --out $MUTSPEC96 --scale -t $HUMANCOUNTS
echo "Collapsed"
if [ ! -e $MUTSPEC96 ]; then
    echo "Error! File '$MUTSPEC96' not found!"
    exit 0
fi

# 3 Deconvolute mutation spectra and get mutation signatures
python3 scripts/signature_extraction.py -m 10 --mutspec $MUTSPEC96 --outdir $SIGDIR
echo "Extraction done"
if [ ! -e $SIGDIR ]; then
    echo "Error! File '$SIGDIR' not found!"
    exit 0
fi

# Decompose on custom database
python3 scripts/decompose.py 
TODO end this script
