import anndata
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt

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

perc_expr = []
dataset_name = []
for datasetname, adata in full_data.items():
    perc_expr += list((adata.X > 0).mean(axis=1))
    dataset_name += [datasetname] * adata.X.shape[0]
sns.violinplot(y=perc_expr, x=dataset_name)
plt.ylabel('Gene/Protein expression completeness per cell')
plt.savefig(snakemake.output[0], bbox_inches='tight')