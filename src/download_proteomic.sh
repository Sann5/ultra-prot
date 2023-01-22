#!/bin/bash

# Make dir 
mkdir -p data/raw/proteomic
cd data/raw/proteomic

# Download data
echo "This can take a while..."
wget https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD024043/DIANN1.8_SingleCells_CellCycle.7z

# Unzip an deleate useless data
tar -xf DIANN1.8_SingleCells_CellCycle.7z
mv DIANN1.8_SingleCells_CellCycle/* ./
rm DIANN1.8_SingleCells_CellCycle*
ls | grep -vE 'cellcyclepred|notnormalized' | xargs rm
