import anndata
import scanpy as sc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap

plt.style.use('seaborn-colorblind')
plt.rc('xtick', labelsize=11)
plt.rc('ytick', labelsize=11)
plt.rcParams.update({'font.size': 11})

full_data = {
    'Proteins': anndata.read_h5ad(filename=snakemake.input[0]), 
    'SMART-Seq2': anndata.read_h5ad(filename=snakemake.input[1]),
    'Drop-Seq': anndata.read_h5ad(filename=snakemake.input[2]),
}

for adata in full_data.values():
    sc.pp.filter_cells(adata, min_genes=600)
    sc.pp.filter_genes(adata, min_cells=0.15 * adata.shape[0])

for name, adata in full_data.items():
    if name != 'Proteins':
        sc.pp.normalize_total(adata, target_sum=np.mean(np.nansum(adata.X, axis=1)))
    sc.pp.log1p(adata.X)

for adata in full_data.values():
    np.random.shuffle(adata.X)

joined = anndata.concat(full_data.values()) # performs inner join
dataset_names = np.concatenate([[name] * adata.shape[0] for name, adata in full_data.items()])
print('number of shared genes:', joined.shape[1])

c = np.array(pd.DataFrame(joined.X.T).corr())

top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Oranges', 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='OrangeBlue')

fig, ax = plt.subplots(3, 3, figsize=(5,5), gridspec_kw=dict(wspace=.03, hspace=.03))
for i, dataset_1 in enumerate(full_data.keys()):
    for j, dataset_2 in enumerate(full_data.keys()):
        subdata = c[dataset_names == dataset_1][:, dataset_names == dataset_2]
        color_obj = ax[i, j].imshow(subdata, vmin=-1, vmax=1, aspect='auto', cmap=newcmp)
        ax[i, j].set_xticks([])
        ax[i, j].set_yticks([])
        if i == 0:
            ax[i, j].set_title(dataset_2, fontsize=11)
        if j == 0:
            ax[i, j].set_ylabel(dataset_1, fontsize=11)

cbar_ax = fig.add_axes([.92, 0.15, 0.05, .7])
plt.colorbar(color_obj, cax=cbar_ax)

plt.savefig(snakemake.output[0], bbox_inches='tight')