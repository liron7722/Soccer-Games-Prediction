import numpy as np
import pandas as pd
from time import time
from sklearn.metrics import r2_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import myFunction as myF


myPath = 'c:\\Users\\Liron\\Desktop\\Projects\\Soccer Games Prediction\\'


data = myF.getMyData(myPath + 'projectdata.csv')
df_Teams = pd.read_csv(myPath + 'df_Teams.csv')
df_Referee = pd.read_csv(myPath + 'df_Referee.csv')


addNewGame = False
toSave = False
if addNewGame:
    LastWeekGames = 'LastWeekGames.csv'
    newFixtures = pd.read_csv(LastWeekGames)
    DivList = ['E0', 'E1', 'F1', 'F2', 'D1', 'D2', 'I1', 'I2', 'SP1', 'SP2']
    for div in DivList:
        newGames = newFixtures[newFixtures['Div'] == div]
        newGames = newGames.fillna(0)
        myF.games(newGames)
    if toSave:
        data.to_csv(myPath + 'projectdata.csv', index=False, sep=',')


dropBeforTrain = ['Date','HomeTeam','AwayTeam','FTR','HTGD','HTR'
                 ]
train = data.drop(dropBeforTrain, axis=1)
train.apply(pd.to_numeric)
train= train.fillna(0)
train.head()


target = 'FTGD'
X = train.drop(target, axis=1).values
y = train[target].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=150)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.3, random_state=150)


# Takes around 30-60 minutes
t1 = time()
# Printing t1 to know when it started
print(time())
RFR = RandomForestRegressor()
parameters = {'n_estimators': [5,10,20,50],#,100,500],
              #'criterion': ['mse'],
              'max_depth': [5, 10, 15],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1,5]
             }

# Run the grid search
grid_obj = GridSearchCV(RFR, parameters,
                        cv=7,
                        n_jobs=-1,
                        verbose=1)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
RFR = grid_obj.best_estimator_

# Fit the best algorithm to the data.
RFR.fit(X_train, y_train)

# Printing time difference to know how much time it took
print((time() - t1)/3600,' Hours')


t1=time()
print_Flag = True
y_pred = RFR.predict(X_test)
if print_Flag:
    print('----------RandomForestRegressor Classifier----------')
    print("ACCURACY SCORE: ", RFR.score(X_test, y_test))
    print("K-Fold Cross Validation Accuracy Score :", np.mean(cross_val_score(RFR, X_train, y_train, cv=7, scoring='accuracy')))
    print("It took {:.2f} seconds".format(time() - t1))


newdf = pd.DataFrame()
isHistory = False

# new Games
url = 'http://www.football-data.co.uk/fixtures.csv'
newGames = pd.read_csv(url)

# adding missing cols befor sending to games function
colList = ['HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']
for col in colList:
    newGames[col] = 0

newGames.to_csv("fixtures.csv", index=False, sep=',')
newFixtures = pd.read_csv('fixtures.csv')

DivList = ['E0', 'E1', 'F1', 'F2', 'D1', 'D2', 'I1', 'I2', 'SP1', 'SP2']
for div in DivList:
    newGames = newFixtures[newFixtures['Div'] == div]
    newGames = newGames.fillna(0)
    myF.games(newGames)
    newData = myF.getNewData(newGames)
    newdf = newdf.append(newData)
newdf.to_csv("AllnewFixtureData.csv", index=False, sep=',')


# newData = pd.read_csv('AllnewFixtureData.csv')
newdf


dropBeforPredicte = ['Date','HomeTeam','AwayTeam','FTR','HTGD','HTR', 'FTGD']
GDP = newdf.drop(dropBeforPredicte, axis=1)
GDP.apply(pd.to_numeric)
X = GDP.values
predictions = RFR.predict(X)


result = pd.DataFrame()
if isHistory:
    colForResult = ['Date','HomeTeam','AwayTeam','FTR', 'FTGD']#,'Referee']
else:
    colForResult = ['Date','HomeTeam','AwayTeam']#,'Referee']
result[colForResult] = newdf[colForResult]
result["GDPredictions"] = np.around(predictions)#Rounded up
result["True_GDPredictions"] = predictions
result = result.reset_index(drop=True)
result.to_csv("result.csv", index=False, sep=',')
result


if isHistory:
    count = 0
    for i in range (len(result)):
        if result["GDPredictions"][i] > 0 and result["FTGD"][i] > 0:
            count += 1
        elif result["GDPredictions"][i] == 0 and result["FTGD"][i] == 0:
            count += 1
        elif result["GDPredictions"][i] < 0 and result["FTGD"][i] < 0:
            count += 1

    print("The Wining Side Predictions is Cuurect: ",count,"/",len(result))
    result.head(10)