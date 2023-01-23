import anndata

# load data from "The transcriptome dynamics of single cells during the cell cycle"

adata1_exon = anndata.read_text(snakemake.input[0]).transpose()
adata1_intron = anndata.read_text(snakemake.input[1]).transpose()
adata2_exon = anndata.read_text(snakemake.input[2]).transpose()
adata2_intron = anndata.read_text(snakemake.input[3]).transpose()

intersection = list(set(adata1_exon.var_names).intersection(adata1_intron.var_names))
intersection_part = adata1_exon[:, intersection].copy()
intersection_part.X += adata1_intron[:, intersection].X
adata1_2 = anndata.concat(
    [
        intersection_part,
        adata1_exon[
            :,
            [
                gene
                for gene in adata1_exon.var_names
                if gene not in adata1_intron.var_names
            ],
        ],
        adata1_intron[
            :,
            [
                gene
                for gene in adata1_intron.var_names
                if gene not in adata1_exon.var_names
            ],
        ],
    ],
    axis=1,
)

intersection = list(set(adata2_exon.var_names).intersection(adata2_intron.var_names))
intersection_part = adata2_exon[:, intersection].copy()
intersection_part.X += adata2_intron[:, intersection].X
adata2_2 = anndata.concat(
    [
        intersection_part,
        adata2_exon[
            :,
            [
                gene
                for gene in adata2_exon.var_names
                if gene not in adata2_intron.var_names
            ],
        ],
        adata2_intron[
            :,
            [
                gene
                for gene in adata2_intron.var_names
                if gene not in adata2_exon.var_names
            ],
        ],
    ],
    axis=1,
)

# second dataset from "The transcriptome dynamics of single cells during the cell cycle"

adata_exon = anndata.read_text(snakemake.input[4]).transpose()
adata_intron = anndata.read_text(snakemake.input[5]).transpose()

intersection = list(set(adata_exon.var_names).intersection(adata_intron.var_names))
intersection_part = adata_exon[:, intersection]
intersection_part.X += adata_intron[:, intersection].X
adata1_3 = anndata.concat(
    [
        intersection_part,
        adata_exon[
            :,
            [
                gene
                for gene in adata_exon.var_names
                if gene not in adata1_intron.var_names
            ],
        ],
        adata_intron[
            :,
            [
                gene
                for gene in adata_intron.var_names
                if gene not in adata1_exon.var_names
            ],
        ],
    ],
    axis=1,
)
adata1_3.var_names_make_unique()

tenx_adata = anndata.concat(
    [adata1_2, adata2_2, adata1_3], join="outer", fill_value=0.0
)

tenx_adata.write(filename=snakemake.output[0])
