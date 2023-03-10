import anndata
import scanpy as sc
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import pyplot_settings
from pyplot_settings import color

full_data = {
    "Proteins": anndata.read_h5ad(filename=snakemake.input[0]),
    "SMART-Seq2": anndata.read_h5ad(filename=snakemake.input[1]),
    "Drop-Seq": anndata.read_h5ad(filename=snakemake.input[2]),
}

core_proteins = list(pd.read_csv(snakemake.input[3], sep="\t")["Genes"])

for adata in full_data.values():
    sc.pp.filter_cells(adata, min_genes=600)
    sc.pp.filter_genes(adata, min_cells=0.15 * adata.shape[0])

for name, adata in full_data.items():
    if name != "Proteins":
        sc.pp.normalize_total(adata, target_sum=np.mean(np.nansum(adata.X, axis=1)))

cov = []
hue = []
dataset_name = []

for datasetname, adata in full_data.items():
    adata.var["core/noncore"] = [
        "Core proteome genes" if prot in core_proteins else "Other proteins"
        for prot in adata.var_names
    ]
    mean = np.nanmean(adata.X, axis=0)
    coeff_of_var = scipy.stats.variation(adata.X, nan_policy="omit").data
    cov += list(coeff_of_var)
    hue += list(adata.var["core/noncore"])
    dataset_name += [datasetname] * adata.shape[1]

sns.boxplot(
    x=dataset_name,
    y=cov,
    hue=hue,
    palette=color,
    showfliers=False,
)
plt.ylabel("coefficient of variation")
plt.ylim(top=6)
plt.savefig(snakemake.output[0], bbox_inches="tight")
