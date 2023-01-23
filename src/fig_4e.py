import anndata
import scanpy as sc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics

plt.style.use('seaborn-colorblind')
plt.rc('xtick', labelsize=11)
plt.rc('ytick', labelsize=11)
plt.rcParams.update({'font.size': 11})

adata = anndata.read_h5ad(filename=snakemake.input[0])
sc.pp.filter_cells(adata, min_genes=600)
sc.pp.filter_genes(adata, min_cells=0.7 * adata.shape[0])
sc.pp.log1p(adata)
adata.X = np.nan_to_num(adata.X)

adata.obs['cell cycle stage'] = [
    'G1' if '_G1_' in name
    else 'G1-S' if '_TB_' in name
    else 'G2' if '_G2_' in name
    else 'G2-M' if '_NB_' in name
    else 'other'
    for name in adata.obs_names
]
adata = adata[adata.obs['cell cycle stage'] != 'other']

cc_markers = pd.read_excel(snakemake.input[1], "Tami_Geiger")

g1_list = cc_markers['G1'][1:-1]
g1_list = [g for g in g1_list if g in adata.var_names]
print(f'G1:\t {", ".join(g1_list)}')

s_list = cc_markers['S'][1:-1]
s_list = [g for g in s_list if g in adata.var_names]
print(f'S:\t {", ".join(s_list)}')

g2m_list = cc_markers['G2M'][1:-1]
g2m_list = [g for g in g2m_list if g in adata.var_names]
print(f'G2M:\t {", ".join(g2m_list)}')

sc.tl.score_genes(adata, g1_list, score_name='g1')
sc.tl.score_genes(adata, s_list, score_name='s')
sc.tl.score_genes(adata, g2m_list, score_name='g2m')

protein_data_nb_tb = adata[np.array(adata.obs['cell cycle stage'] == 'G2-M') 
                                  | np.array(adata.obs['cell cycle stage'] == 'G1-S')]

score = {
    'G2-M': protein_data_nb_tb.obs['g2m'].values,
    'S': protein_data_nb_tb.obs['s'].values,
    'G1': protein_data_nb_tb.obs['g1'].values
}

for phase in score.keys():
    true_label = np.array([phase in a for a in protein_data_nb_tb.obs['cell cycle stage'].values])
    scores = score[phase]
    fp, tp, _ = sklearn.metrics.roc_curve(true_label, scores)
    plt.plot(fp, tp, label=phase)
plt.plot([0, 1], [0, 1], c='black')
plt.gca().set_aspect('equal')
plt.xlabel('False-positive')
plt.ylabel('True-positive')
plt.legend()
plt.title('G2-M vs G1-S')
plt.savefig(snakemake.output[0])