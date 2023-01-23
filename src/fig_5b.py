import anndata
import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt
import pyplot_settings

full_data = {
    "Proteins": anndata.read_h5ad(filename=snakemake.input[0]),
    "SMART-Seq2": anndata.read_h5ad(filename=snakemake.input[1]),
    "Drop-Seq": anndata.read_h5ad(filename=snakemake.input[2]),
}

for adata in full_data.values():
    sc.pp.filter_cells(adata, min_genes=600)
    sc.pp.filter_genes(adata, min_cells=0.15 * adata.shape[0])

shared_genes = set(full_data["Proteins"].var_names)
for adata in full_data.values():
    shared_genes = shared_genes.intersection(adata.var_names)

intersection_data = {
    datasetname: adata[:, list(shared_genes)]
    for datasetname, adata in full_data.items()
}

for adata in intersection_data.values():
    adata.X = np.nan_to_num(adata.X)
    sc.pp.normalize_total(adata, target_sum=1e6)
    sc.pp.log1p(adata.X)

for datasetname, adata in intersection_data.items():
    adata.obs["dataset"] = datasetname
joined = anndata.concat([adata for adata in intersection_data.values()])

sc.pp.pca(joined)
ax = sc.pl.pca(joined, color="dataset", show=False, annotate_var_explained=True)
ax.invert_xaxis()
plt.savefig(snakemake.output[0], bbox_inches="tight")
