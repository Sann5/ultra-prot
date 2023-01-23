import anndata
import scanpy as sc
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pyplot_settings
plt.rcParams.update({'font.size': 11})

adata_raw = anndata.read_h5ad(filename=snakemake.input[0])
sc.pp.filter_cells(adata_raw, min_genes=600)
sc.pp.filter_genes(adata_raw, min_cells=0.15 * adata_raw.shape[0])

adata_raw.obs['cell cycle stage'] = [
    'G1' if '_G1_' in name
    else 'G1-S' if '_TB_' in name
    else 'G2' if '_G2_' in name
    else 'G2-M' if '_NB_' in name
    else 'other'
    for name in adata_raw.obs_names
]

size = {cond: adata_raw[adata_raw.obs['cell cycle stage'] == cond].X.sum(axis=1)
       for cond in ['G1', 'G1-S', 'G2', 'G2-M']}
x = np.concatenate([[cond] * len(cells) for cond, cells in size.items()])
y = np.concatenate([cells for cells in size.values()])
sns.boxplot(x=x, y=y)
plt.xlabel("Cell cycle stage")
plt.ylabel("Raw MS signal")

plt.savefig(snakemake.output[0])