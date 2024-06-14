# LaySummarization_TFG

## Dataset

The data used for this TFG can be found in the following link: https://github.com/TGoldsack1/Corpora_for_Lay_Summarisation 
- DataExploration.ipynb: our own exploratory data analysis conducted in a Google Colaboratory notebook

## Training
- Bart_finetuning_TrainerAPI.ipynb: this notebook contains the code to train [Abstract], [Whole text] and [Whole text no refs] models

## Evaluation

The evaluation models and scrips can be found in the following link: https://github.com/TGoldsack1/BioLaySumm2024-evaluation_scripts. We had to perform two changes in the scripts:
- Change the path to the models to specify our path.
- Comment the evaluation of the results with LENS and BERTScore due to library dependencies problems.
