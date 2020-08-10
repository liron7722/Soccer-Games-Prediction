# Soccer Leagues Match Prediction
# Personal Project
# By: Liron Revah

# Background - Read ME
# This Project started by me for a course i had in the second year for my degree
# This is the improved version
# This project meant for study only
# In case you reading this you should be warned this isn't a perfect Algorithm
# You are taken a risk by using this for gambling
# Remember hard work is greater then gambling

import myFunction as myF

# create better data set
df = myF.readStats()
myF.saveStats(df)
data, df_Teams, df_Referee = myF.Initilize()
myF.games(df)
myF.saveDataSet()
myF.save_df_Teams()
# myF.save_df_Referee()
