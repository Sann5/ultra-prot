import pandas as pd
import numpy as np
import anndata

path_to_file = snakemake.input[0]

cols = list(pd.read_csv(path_to_file, nrows=1, sep="\t"))
prot = pd.read_csv(
    path_to_file, usecols=[i for i in cols if "TSCP_DIA_SingleCell" in i], sep="\t"
)
var_annotation = pd.read_csv(
    path_to_file, index_col="Genes", usecols=["Genes"], sep="\t"
)

if "20210919_DIANN_SingleCellOutput.pg_matrix_notnormalized" in path_to_file:
    prot = prot.fillna(0.0)
    prot[prot == "Filtered"] = 0.0
else:
    prot[prot == "Filtered"] = np.nan

adata_prot_raw = anndata.AnnData(prot.transpose())
adata_prot_raw.var = var_annotation
adata_prot_raw.var_names = adata_prot_raw.var_names.map(str)
adata_prot_raw.var_names_make_unique()

adata_prot_raw.write(filename=snakemake.output[0])
