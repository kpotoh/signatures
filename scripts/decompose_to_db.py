from SigProfilerAssignment import Analyzer as Analyze

signatures  = "data/processed/sars-cov-2-normed-on-human/SBS96/Suggested_Solution/SBS96_De-Novo_Solution/Signatures/SBS96_De-Novo_Signatures.txt"
samples     = "data/sars-cov-2_96.tsv"
output      = "data/output_example/decomp"
sigs = None
# sigs        = "COSMIC_v3_SBS_GRCh37_noSBS84-85.txt" #  Custom Signature Database


# for sars-cov-2
signature_subgroups = [
    'remove_Artifact_signatures', 
    'remove_HR_deficiency_signatures' ,
    'remove_POL_deficiency_signatures',
    'remove_BER_deficiency_signatures',
    'remove_Chemotherapy_signatures',
    'remove_MMR_deficiency_signatures',
     
    # 'remove_APOBEC_signatures', 
    # 'remove_Tobacco_signatures', 
    # 'remove_UV_signatures', 
    # 'remove_AA_signatures',
    # 'remove_Colibactin_signatures', 
    # 'remove_Lymphoid_signatures'
]

# Parameners
# samples - mutspec  (mutation types * sample IDs)
# signatures         (mutation types * signature IDs)
# activities         (sample IDs * signature IDs)


# Decomposes the De Novo Signatures into COSMIC Signatures and assigns COSMIC signatures into samples
print("decompose_fit...")
Analyze.decompose_fit( samples, 
                       output, 
                       signatures=signatures,
                       signature_database=sigs,
                       genome_build="GRCh37", 
                       new_signature_thresh_hold=0.8,
                       signature_subgroups=signature_subgroups,
                       connected_sigs=True)

# Attributes mutations of given Samples to input COSMIC signatures. 
# Note that penalties associated with denovo fit and COSMIC fits are different. drawing
print("cosmic_fit...")
Analyze.cosmic_fit( samples, 
                    output, 
                    signatures=None,
                    signature_database=sigs,
                    genome_build="GRCh37", 
                    collapse_to_SBS96=False,
                    signature_subgroups=signature_subgroups,
                    connected_sigs=True)
