import anndata

adata1 = anndata.read_text(snakemake.input[0]).transpose()
adata2 = anndata.read_text(snakemake.input[1]).transpose()
adata3 = anndata.read_text(snakemake.input[2]).transpose()
adata3.var_names = adata1.var_names
adata2 = adata2[:, adata1.var_names] # without ERCC genes
smartseq_adata = anndata.concat([adata1, adata2, adata3])

smartseq_adata.write(
    filename=snakemake.output[0]
)