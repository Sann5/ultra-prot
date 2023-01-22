rule preprocess_proteomic:
    input:
        "data/raw/proteomic/{sample}.tsv"
    output:
        "data/preprocessed/proteomic/{sample}.h5ad"
    script:
        "src/preprocess_proteomic.py"

rule preprocess_transcriptomic_study_1:
    input:
        "data/raw/transcriptomic/study_1/GSM3713084_HeLa_1.txt",
        "data/raw/transcriptomic/study_1/GSM3713085_HeLa_2.txt",
        "data/raw/transcriptomic/study_1/GSM3713086_HeLa_3.txt"
    output:
        "data/preprocessed/transcriptomic/GSM3713084_HeLa.h5ad"
    script:
        "src/preprocess_transcriptomic_study_1.py"

rule preprocess_transcriptomic_study_2:
    input:
        "data/raw/transcriptomic/study_2/GSM4224315_out_gene_exon_tagged.dge_exonssf002_WT.txt",
        "data/raw/transcriptomic/study_2/GSM4224315_out_gene_exon_tagged.dge_intronssf002_WT.txt",
        "data/raw/transcriptomic/study_2/GSM4224316_out_gene_exon_tagged.dge_exonssf002_KO.txt",
        "data/raw/transcriptomic/study_2/GSM4224316_out_gene_exon_tagged.dge_intronssf002_KO.txt",
        "data/raw/transcriptomic/study_2/GSM4226257_out_gene_exon_tagged.dge_exonsds_046.txt",
        "data/raw/transcriptomic/study_2/GSM4226257_out_gene_exon_tagged.dge_intronsds_046.txt"
    output:
        "data/preprocessed/transcriptomic/GSM4226257_out_gene_exon_tagged.h5ad"
    script:
        "src/preprocess_transcriptomic_study_2.py"

rule fig_4c:
    input:
        "data/preprocessed/proteomic/20210919_DIANN_SingleCellOutput.pg_matrix_notnormalized.h5ad"
    output:
        "results/fig_4c.png"
    script:
        "src/fig_4c.py"
        