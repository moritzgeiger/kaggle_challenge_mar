# Data analysis
- Document here the project: **Tabular Playground Series - Mar 2021**
- Description: This project aims to predict a binary target. The challenge is released once a month by Kaggle and open for everyone. As training data there is a total of **300,000 observations** with 30 features. 11 features are continuous values (standardized) and 19 features are categorical. The distribution of the latter is quite unbalanced and therefore needs some preprocessing. The target of 0 and 1 is also **unbalanced**, leaning towards skewed to 1. To balance the data the oversampling techinque of SMOTE is used. The notebook **'mg_pipeline'** goes through the common preprocessing and encoding strategies. As a final estimator the **RandomForestClassifier** from ScikitLearn is chosen.
- Data Source: https://www.kaggle.com/c/tabular-playground-series-mar-2021/data
- Scorer: ```f1```
- Type of analysis: Logistic Regression


# Startup the project

- Download the provided data from [Kaggle](https://www.kaggle.com/c/tabular-playground-series-mar-2021/data). Or use the direct download CLI command ```kaggle competitions download -c tabular-playground-series-mar-2021```

- Go to the Challenge on Kaggle: <a href="https://www.kaggle.com/c/tabular-playground-series-mar-2021">Link</a>
- upload the test.csv klick Predict & Download
- You will have the predictions ready for submission in your download folder

# Summary
- A predictor with a simple model in production
- The overall Kaggle score for this predictor is 0.77836
- Go to <a href="kaggle-predictor-mar.herokuapp.com">kaggle-predictor-mar.herokuapp.com</a> to have your own prediction
