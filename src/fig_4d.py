import anndata
import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt
import pyplot_settings


def impute_downshifted_normal_global(
    adata,
    scale=0.3,
    shift=1.8,
):
    np.random.seed(42)
    mean = np.nanmean(adata.X)
    std = np.nanstd(adata.X)
    draws = np.random.normal(
        loc=mean - shift * std, scale=scale * std, size=np.sum(np.isnan(adata.X))
    )
    adata.X[np.isnan(adata.X)] = draws


adata = anndata.read_h5ad(filename=snakemake.input[0])
sc.pp.filter_cells(adata, min_genes=600)
sc.pp.filter_genes(adata, min_cells=0.15 * adata.shape[0])
sc.pp.log1p(adata)
impute_downshifted_normal_global(adata)

adata.obs["cell cycle stage"] = [
    "G1"
    if "_G1_" in name
    else "G1-S"
    if "_TB_" in name
    else "G2"
    if "_G2_" in name
    else "G2-M"
    if "_NB_" in name
    else "other"
    for name in adata.obs_names
]
adata = adata[adata.obs["cell cycle stage"] != "other"]

sc.pp.pca(adata)
sc.pl.pca(adata, color="cell cycle stage", annotate_var_explained=True, show=False)
plt.savefig(snakemake.output[0], bbox_inches="tight")
