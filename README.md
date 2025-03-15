# Assessing workflow impact and clinical utility of AI-assisted brain aneurysm detection: a multi-reader study
<p float="middle">
  <img src="https://github.com/connectomicslab/AI-Assisted-Aneurysm-Detection/blob/main/images/AI_assisted_scenario.png" width="700"/>
</p>

This repository contains the code for the paper: "Assessing workflow impact and clinical utility of AI-assisted brain
aneurysm detection: a multi-reader study".

## Installation/Softwares
The results of the paper were obtained with python 3.9 and a Windows OS. Reproducibility for different configurations is not guaranteed.
For the R scripts, we used RStudio 2022.07.2. For the creation of the overlay dicom series, we used MeVisLab 3.4.2.

### Setup conda environment
To run the python scripts:
1) Clone the repository
2) Create a conda/pip environment and installed all required packages. If you are not familiar with pip/conda environments, please check out the [official documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
Alternatively, feel free to use your favorite [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) such as [PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux) or [Visual Studio Code](https://code.visualstudio.com/) to set up an environment.

## Data
The majority of the dataset used for this study can be downloaded from this
[OpenNEURO link](https://openneuro.org/datasets/ds003949).
The files containing the results of the two readings, both for the junior and senior radiologists,
are located inside the directory `READINGS`.

## Usage
### Overlay Series Generation
The code used to generate the DICOM overlay series where the segmentations are overlayed on the TOF-MRA volumes is 
called `d20221006_export_fused_images.mlab` and is located inside the directory `mevislab_overlay`.
### Sensitivity and Specificity Analyses
To code used to run the McNemar's tests for the sensitivity and specificity analyses presented in the paper is
located in the directory `sensitivity_specificity_analysis_R`
### Reading time
The script used to compare the reading times of the two radiologists with and without the assistance
of the CAD is called `compare_timing_between_readings.py` and is located inside the directory `reading_time`.
The files containing the results of the two readings (which include the reading times) are located inside
the directory `READINGS`.
### Confidence scores
All the scripts related to the confidence scores are located in the directory `confidence_score`. 
To script used to create the barplots that display the confidence scores is `d20240916_confidence_scores_barplots.py`.
To script used to run the XYZ test to compare the distributions of confidence scores is `TO_ADD`


## How to cite
If you're using our dataset/model or comparing performances with the ones presented in this work, please cite the following publications:

        [1] Di Noto, T., Marie, G., Tourbier, S., Alemán-Gómez, Y., Esteban, O., Saliou, G., ... & Richiardi, J. (2023). Towards automated brain aneurysm detection in TOF-MRA: open data, weak labels, and anatomical knowledge. Neuroinformatics, 21(1), 21-34.

and
        TODO: add (med)-arxiv once it's public
