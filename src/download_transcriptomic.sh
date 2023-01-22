#!/bin/bash

# Make dirs
mkdir -p data/raw/transcriptomic
cd data/raw/transcriptomic
mkdir study_1 study_2

# Download
# Study 1
cd study_1
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM3713nnn/GSM3713086/suppl/GSM3713086_HeLa_3.txt.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM3713nnn/GSM3713085/suppl/GSM3713085_HeLa_2.txt.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM3713nnn/GSM3713084/suppl/GSM3713084_HeLa_1.txt.gz

# Unzip
for all in *.gz; do gunzip $all; done

# Study 2
cd ../study_2
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4224nnn/GSM4224316/suppl/GSM4224316_out_gene_exon_tagged.dge_intronssf002_KO.txt.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4224nnn/GSM4224316/suppl/GSM4224316_out_gene_exon_tagged.dge_exonssf002_KO.txt.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4224nnn/GSM4224315/suppl/GSM4224315_out_gene_exon_tagged.dge_intronssf002_WT.txt.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4224nnn/GSM4224315/suppl/GSM4224315_out_gene_exon_tagged.dge_exonssf002_WT.txt.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4226nnn/GSM4226257/suppl/GSM4226257_out_gene_exon_tagged.dge_exonsds_046.txt.gz 
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM4226nnn/GSM4226257/suppl/GSM4226257_out_gene_exon_tagged.dge_intronsds_046.txt.gz 

# Unzip
for all in *.gz; do gunzip $all; done