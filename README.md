Analysis of COVID19 chest X-rays
==============================

This README.md file explains the content of this repository. 


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Should be in your computer but not on Github (only in .gitignore)
    │   ├── processed      <- processed data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- best trained model
    │
    │
    ├── notebooks                       <- Jupyter notebooks.  
    │   │                               <- code of the final model
    │   ├── experimentations            <- code of all the experiexperimentations during the project  
    │   │   ├── deep_learning           <- deep laerning tests 
    │   │   │   ├── data_preprocessing  <- code to preprocess the data 
    │   │   │   └── model_testing       <- code to do modeling
    │   │   ├── machine_learning        <- machine learning test
    │   │   │   ├── data_preprocessing  <- code to preprocess the data 
    │   │   │   └── model_testing       <- code to do modeling
    │   
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- Contains the final versions of the 3 reports as pdf
    │   └── latex          <- tex-files to generate the pdf reports
    │   └── figures        <- Generated graphics and figures used in the reports
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

------------

Data / Image Organization
------------

It is important to follow the structure from above `Project Organization` to ensure all participants could work with the sources in the same way! So avoid using absolute pathes in the source code is important - use relative paths instead! The folder `data` is alreade configured in `.gitignore` file and will not be included into the git repository.

The downlaoded dataset (archive.zip) need to be downloded and copied to `data/raw` folder. Then un-zip it there, as a result there is a new subfolder: `COVID-19_Radiography_Dataset`. 

Any data and/or ouput generated from our source code must be stored in: `data/raw/processed`

Sample folder structure
```
    ├── data
    │   ├── processed
    │   |   ├── converted_grayscale
    │   |   ├── normalized_xrays
    │   |   ├── processed_xrays
    │   |   └── *.csv, *.xlsx, *,npz, etc.
    │   └── raw
    │       ├── COVID-19_Radiography_Dataset
    │       └── archive.zip
```


------------

Models
------------

In the "models" folder the final pretrained model, we chose in this project, is saved. 


------------

Notebooks
------------

In the "notebooks" folder you can access the jupyter notebooks which were used and created during this project. 
The head folder "notebooks" contains the jupyter notebooks which refer to the final model we chose. 
In addition, there is the folder "experimentations", which contains all jupyther nootbooks that were used for the experimentation phase. These jupyter nootbooks are divided into machine and deep learning with each folder having a subfolder for data preprocessing and modelling.

------------

Reports
------------

The "reports" folder contains the final versions of the three reports of this project. The subdolder "latex" contains the tex-files to generate the pdf reports and the subfolder "figures" contains all the figures which are included in the three reports.

------------

src
------------

This folder is not used within this project.


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

