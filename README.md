# LaySummarization_TFG

## Dataset

The data used for this TFG can be found in the following link: https://github.com/TGoldsack1/Corpora_for_Lay_Summarisation 
- DataExploration.ipynb: our own exploratory data analysis conducted in a Google Colaboratory notebook

## Training
- requirements.txt: the libraries needed to execute the trainings 
- Bart_finetuning_TrainerAPI.ipynb: this notebook contains the code to train [Abstract], [Whole text], and [No refs] models
- Bart_finetuning_extractive.ipynb: this notebook contains the code to train [TextRank] and [No refs + TextRank]
- Bart_finetuning_extractive-sections.ipynb: this notebook contains the code to train [TextRank by sections] and [No refs + TextRank by sections]
- Monitoring-ipynb: contains the code used to monitor CPU and GPU resources consumption
- utils.py: contains multiple functions used in several notebooks

## Evaluation

- Prediction_generation.ipynb: contains the code to generate predictions from the models
- Evaluation.ipynb: using the evaluation scripts provided by the organization we evaluate our models' predictions

The evaluation models and scrips can be found in the following link: https://github.com/TGoldsack1/BioLaySumm2024-evaluation_scripts. We had to perform two changes in the scripts:
- Change the path to the models to specify our path.
- Comment the evaluation of the results with LENS and BERTScore due to library dependencies problems.
