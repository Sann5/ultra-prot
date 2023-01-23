import anndata
import scanpy as sc
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy 
import pyplot_settings
from pyplot_settings import color

adata = anndata.read_h5ad(filename=snakemake.input[0])
sc.pp.filter_cells(adata, min_genes=600)
sc.pp.filter_genes(adata, min_cells=0.15 * adata.shape[0])

core_proteins = list(pd.read_csv(snakemake.input[1], sep='\t')['Genes'])

adata.var['core/noncore'] = [
    'Core proteome genes' if prot in core_proteins 
    else 'Other proteins' 
    for prot in adata.var_names
]
mean = np.nanmean(adata.X, axis=0)
coeff_of_var = scipy.stats.variation(adata.X, nan_policy='omit').data

g = sns.JointGrid(
    x=np.log2(mean),
    y=np.log2(coeff_of_var),
    hue=adata.var['core/noncore'],
    palette=color,
)
g.plot_joint(
    sns.scatterplot, 
    s=10, 
    alpha=1,
    linewidth=.1
)
g.plot_marginals(
    sns.histplot, 
    kde=True, 
    stat='density', 
    common_norm=False,
    binwidth=.2,
    alpha=.8
)
g.ax_joint.set_xlabel('log 2 mean')
g.ax_joint.set_ylabel('log 2 coefficient of variation')
g.ax_joint.set_xlim(-4, 18)
g.ax_joint.set_ylim(-4, 4)
g.ax_joint.plot([-6, 10], [3, -5], '--',c='black', label='Poisson distribution')
g.ax_joint.legend(title=[])
plt.suptitle('Drop-Seq', y=1)
plt.savefig(snakemake.output[0], bbox_inches='tight')