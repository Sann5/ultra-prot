# 🧬 🧪 Ultra-high Sensitivity Mass Spectrometry Single-Cell Proteome Analysis  💻  🔬

This repository contains a **reproduction** of the analysis made in [Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation](https://doi.org/10.15252/msb.202110798), A Brunner, ..., M Mann, Molecular Systems Biology (2022), specifically the analysis contained in the ascoiated GitHub [repository](https://github.com/theislab/singlecell_proteomics).

## Why reproduce the analysis?

We aim to provide the same analysis but in a way in which it falls in line with various standards and best practices. To restructure the analysis, the reproduction uses [Snakemake](https://snakemake.readthedocs.io/en/stable/), a workflow management system that benefits from improved readability, portability, modularization, transparency, scalability. Additionaly we tried to improve the repositary organization and documentation.

## What is the paper about? 📖

**TLDR: new ultrasensitive singe-cell proteiomics experimantal method.**

The authors put forward ultrasensitive mass specrtometry (MS)-based workflow that allows to persicely and accurately quantify the proteome of single cells. To keep things short and sweet, here are the major selling points.

- Ten-fold sensitivity increase.
- Injection of single cells one by one into the MS system allows true single-cell–derived proteomics.

This last feature gives name to their invention; true single-cell–derived proteomics, or T-SCP.

In the second part of the paper -after intoducing the techincal aspects fo thir methodology- the authors show that their method is powerful enough to expose differences in the proteome of cells in different stages of the cell cycle. To do so, they took cells from an inmortalized human cell line (HeLa cells) and treated different cell populations with different substances that would arrest the cell cylce at different stage. Then they used their method to analyze the proteome of individual cells of the different populations and analyze their differences.  

In a third section of the paper, the authors compare the proteomic data with the transcriptomic data of untreated cells of the same lineage. They analyze the expression distributions resulting from both technologies and conclude that the proteome exhibits notably distinct characteristics and therfore it cannot entirely be inferred from proteomic data. This idea supports the thesis that although the transcriptome gives way to the proteome, there are a lot of regulatiory mechanisms that take place in betweeen.

## My Two Cents on The Paper 🪙 🪙

*Disclaimer: the following statement relfects my personal opinion and mine only ("my" referring to the author of this repo).*

The papar spends a significant ammount of using their method test applications, only to confirm what is already thought to be known. I would have spent more effort and content on benchmarking the method.

## Usage

### Create an Environment

Using a virtual environment is strongly recommended. If you use [mamba](https://mamba.readthedocs.io/en/latest/) for example you can create an environment with the following command.

```sh
mamba env create --name <choose_a_name> --file environment.yaml
```

### Running the Analysis

TODO...

## Contributing

Check [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Getting support

Check [SUPPORT.md](.github/SUPPORT.md).

## Credits

This project was created using a template from the [World Bank Development Data Group](https://worldbank.github.io/template/README.html)
