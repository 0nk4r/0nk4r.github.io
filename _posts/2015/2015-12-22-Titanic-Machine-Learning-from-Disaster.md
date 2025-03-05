---
layout: post
title: Titanic&#58; Machine Learning from Disaster
date: 2015-12-22 12:00 +0530
last_modified_at: 2019-11-28 16:34 -0800
tags: [Machine Learning, Kaggle]
matjax: true
---

### Creating a Random Forest model to predict survivors

```python
import graphlab as gl
import numpy as np
import matplotlib.pyplot as plt

# Something is wrong with this so Im commenting it. File a bug report.
#gl.canvas.set_target('ipynb')
%matplotlib inline
plt.rcParams['figure.figsize'] = (15.0, 8.0)
```

### Loading Data into SFrames

```python
titanic_data = gl.SFrame.read_csv('./data/train.csv', column_type_hints={'PassengerId': int, 'Name': str,
                                                                         'Survived': int, 'Pclass': int, 'Sex': str,
                                                                         'Cabin': str, 'Embarked': str, 'Age' : float,
                                                                         'SibSp': int, 'Parch': int, 'Fare' : float})
```

```
[INFO] [1;32m1450731072 : INFO:     (initialize_globals_from_environment:282): Setting configuration variable GRAPHLAB_FILEIO_ALTERNATIVE_SSL_CERT_FILE to C:\Anaconda\envs\dato-env\lib\site-packages\certifi\cacert.pem
[0m[1;32m1450731072 : INFO:     (initialize_globals_from_environment:282): Setting configuration variable GRAPHLAB_FILEIO_ALTERNATIVE_SSL_CERT_DIR to
[0mThis non-commercial license of GraphLab Create is assigned to chenna@outlook.com and will expire on October 18, 2016. For commercial licensing options, visit https://dato.com/buy/.

[INFO] Start server at: ipc:///tmp/graphlab_server-5752 - Server binary: C:\Anaconda\envs\dato-env\lib\site-packages\graphlab\unity_server.exe - Server log: C:\Users\Chenna\AppData\Local\Temp\graphlab_server_1450731073.log.0
[INFO] GraphLab Server Version: 1.7.1


PROGRESS: Finished parsing file D:\Code\Kaggle\Titanic Machine Learning from Disaster\data\train.csv
PROGRESS: Parsing completed. Parsed 100 lines in 0.019012 secs.
PROGRESS: Finished parsing file D:\Code\Kaggle\Titanic Machine Learning from Disaster\data\train.csv
PROGRESS: Parsing completed. Parsed 891 lines in 0.01549 secs.
```

There are 891 lines of train data. So, up to PassesngerId 891 the data belongs
to training dataset and contains survivor data.

```python
# test data too
titanic_data_test = gl.SFrame.read_csv('./data/test.csv', column_type_hints={'PassengerId': int, 'Name': str,
                                                                         'Survived': int, 'Pclass': int, 'Sex': str,
                                                                         'Cabin': str, 'Embarked': str, 'Age' : float,
                                                                         'SibSp': int, 'Parch': int, 'Fare' : float})
```

```
PROGRESS: Finished parsing file D:\Code\Kaggle\Titanic Machine Learning from Disaster\data\test.csv
PROGRESS: Parsing completed. Parsed 100 lines in 0.018012 secs.
PROGRESS: These column type hints were not used: Survived
PROGRESS: Finished parsing file D:\Code\Kaggle\Titanic Machine Learning from Disaster\data\test.csv
PROGRESS: Parsing completed. Parsed 418 lines in 0.015011 secs.
```

```python
titanic_data = titanic_data.join(titanic_data_test, how='outer')
```

```python
print len(titanic_data)
```
```
1309
```

### Clean the Data!

Lets now check what data is missing and what we can do about it.

```python
# using plotly's new offline feature
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go
init_notebook_mode()
```

```python
# helps us get an overview of all the data
titanic_data.show()
```

```
Canvas is accessible via web browser at the URL: http://localhost:1949/index.html
Opening Canvas in default web browser.
```

```python
# Saving the data
titanic_data.save('titanic_data')
```

To find the missing data, we write helper functions which iterate through the
data and find whats missing.

```python
# listing all columns
columns = ["Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

# this can be done better, but for now this is it
column_null = []
column_not_null = []

for c in columns:

    null = 0
    not_null = 0

    for x in titanic_data[c]:
        if (x== None) or (x=='') :
            null += 1
        else: not_null += 1

    column_null.append(null)
    column_not_null.append(not_null)

print column_null
print column_not_null
```

```
[0, 0, 0, 263, 0, 0, 0, 1, 1014, 2]
[1309, 1309, 1309, 1046, 1309, 1309, 1309, 1308, 295, 1307]
```

```python
null_data = go.Bar(
    x=columns,
    y=column_null,
    name='missing data'
)
not_null_data = go.Bar(
    x=columns,
    y=column_not_null,
    name='Available data'
)

missing_data = [not_null_data, null_data]
layout = go.Layout(
    barmode='stack'
)
fig = go.Figure(data=missing_data, layout=layout)
iplot(fig, show_link=False)
```

```
Drawing...
```

```diff
- Plot wont work anymore, I had to remove it.
```

From the plot, we can see there there are **263** datapoints missing from the
**Age** column, **1** missing datapoint from **Fare** column and lots of
missing data from **Cabin** column.

We can use build a regression model to learn the missing age data. Fare data
can be approximated based on the majority or just write it as 0. Cabin data
cannot be approximated or learnt. Hence, we drop this column.

To learn the age data, it would be helpful if we know the persons title, which
can be extracted from Name.

```python
def get_title(name):
    start = name.find(", ") + len(", ")
    end = name.find(". ") + 1
    return name[start:end]

titanic_data["Title"] = titanic_data["Name"].apply(lambda x: get_title(x))

titanic_data["Title"].unique()
```

```
dtype: str
Rows: 18
['Mrs.', 'Mlle.', 'Rev.', 'Don.', 'Col.', 'Dr.', 'Master.', 'Mme.', 'Sir.', 'the Countess.', 'Major.', 'Miss.', 'Jonkheer.', 'Lady.', 'Dona.', 'Ms.', 'Mr.', 'Capt.']
```

There are 18 different unique titles in the dataset. We will now simplify this.

-   young : Mlle. Master. Ms. Miss. Jonkheer.
-   Adult men : Rev. Don. Col. Dr. Sir. Major. Mr. Capt.
-   Adult women : Mrs. Mme. the Countess. Lady. Dona.

source: https://en.wikipedia.org/wiki/Title

```python
def change_title(title):
    if title in ['Mlle.', 'Master.', 'Ms.', 'Miss.', 'Jonkheer.']:
        return 'Young'
    elif title in ['Rev.', 'Don.', 'Col.', 'Dr.', 'Sir.', 'Major.', 'Mr.', 'Capt.']:
        return 'Adult_men'
    else: return 'Adult_women'

titanic_data["Title"] = titanic_data["Title"].apply(lambda x: change_title(x))
```

We will now create a random forest regression model to learn the missing age 
data.

```python
# Fill the missing fare with 0
def changeFare(fare):
    if fare == None:
        return 10.5
    else: return fare

titanic_data['Fare'].apply(lambda x : changeFare(x))

def changeEmbarked(emb):
    if (emb == '') or (emb==None):
        return 'S'
    else: return emb

titanic_data['Embarked'].apply(lambda x : changeEmbarked(x));
```

```python
age_train, age_test = titanic_data[titanic_data['Age']!=None].random_split(0.8, seed=0)

age_model = gl.random_forest_regression.create(age_train, target='Age', num_trees=200,
                                              features=["Pclass", "Name", "Sex",
                                                        "SibSp", "Parch", "Ticket",
                                                        "Fare", "Embarked", "Title"])
```

```
PROGRESS: Random forest regression:
PROGRESS: --------------------------------------------------------
PROGRESS: Number of examples          : 833
PROGRESS: Number of features          : 9
PROGRESS: Number of unpacked features : 9
PROGRESS: Starting Boosted Trees
PROGRESS: --------------------------------------------------------
PROGRESS:   Iter        RMSE Elapsed time
PROGRESS:      0  1.036e+001        0.00s
PROGRESS:      1  1.014e+001        0.01s
...
PROGRESS:    146  9.907e+000        0.34s
PROGRESS:    147  9.905e+000        0.34s
```

```python
# Evaluate the predictions
print age_model.evaluate(age_test)
```

```
{'max_error': 35.518862028968, 'rmse': 10.480427799966918}
```

```python
def fillAge(x):
    return age_model.predict(x)[0]

titanic_data[titanic_data['Age']==None].apply(lambda x: fillAge(x));
```

### Try using a randomforest classifier to predict

```python
train_data = titanic_data[titanic_data['Survived']!=None]
predict_data = titanic_data[titanic_data['Survived']==None]

randFor_titanic = gl.random_forest_classifier.create(train_data, target='Survived', num_trees=2000,max_depth=4,
                                                     features=["Pclass","Age", "Name", "Sex",
                                                        "SibSp", "Parch", "Ticket",
                                                        "Fare", "Embarked", "Title"])
```

```
PROGRESS: Creating a validation set from 5 percent of training data. This may take a while.
          You can set ``validation_set=None`` to disable validation tracking.

PROGRESS: Random forest classifier:
PROGRESS: --------------------------------------------------------
PROGRESS: Number of examples          : 847
PROGRESS: Number of classes           : 2
PROGRESS: Number of feature columns   : 10
PROGRESS: Number of unpacked features : 10
PROGRESS: Starting Boosted Trees
PROGRESS: --------------------------------------------------------
PROGRESS:   Iter      Accuracy          Elapsed time
PROGRESS:         (training) (validation)
PROGRESS:      0  8.489e-001  8.182e-001        0.00s
...
PROGRESS:     62  8.512e-001  8.636e-001        0.09s
```

```python
solution = randFor_titanic.predict(predict_data)
```

```
...
PROGRESS:   1065  8.619e-001  8.182e-001        1.41s
```

```python
solutionToCSV = gl.SFrame()
solutionToCSV['PassengerId'] = predict_data['PassengerId']
solutionToCSV.add_column(solution, name='Survived')

solutionToCSV.save('randomForests.csv', format='csv')
```

This model gives a score of 0.78469. This can be further imporved by adding
extra features like family data, etc.

