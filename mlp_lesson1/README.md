# Introductino to Scikit-learn

## Ch1 Introduction

- `Scikit-learn` focuses on **modelling data**
  - Datasets
  - Supervised models
  - Feature selection
  - Clustering of unlabelled data
  - Dataset transformation
    - Preprocessing
    - Feature extraction
    - Normalisation
    - Dimensionality reduction
  - Model selection and evaluation
    - Cross validation
    - Hyperparameter tuning
    - Classification metrics
  - Ensemble methods
    - Boosting
    - Bagging
    - Random Forest

## Ch2 Classification Pipeline

- Arrange data into `X` and `y`
- Choose the model
- Initialise your model with some hyperparameters
- Fit model to `X` and `y`
- Predict labels `y_hat_test` for `X_test`
- Evaluate model performance by comparing `y_hat_test` against `y_test`

## Ch5 Preprocessing

- `preprocessing.scale(x)`
  - Scale to **zero mean** and **unit variance**
- `preprocessing.MinMaxScalar().fit_transform(x)`
  - Scale values from 0 to 1

## Ch6 Classification Models

- **kNN**
  - `sklearn.neighbors` - `KNeighborClassifier`
- **Decision Tree**
  - `sklearn.tree` - `DecisionTreeClassifier`
- **Logistic Regression**
  - `sklearn.linear_model` - `LogisiticRegression`
- **Random Forests**
  - `sklearn.ensemble` - `RandomForestClassifier`
- **Naive Bayes** (Gaussian)
  - `sklearn.ensemble` - `GaussianNB`
- **Support Vector Machine**
  - `sklearn.svm` - `SVC`
- **Multiplayer Perceptron** (Neural Nets)
  - `sklearn.neural_network` - `MLPClassifier`
