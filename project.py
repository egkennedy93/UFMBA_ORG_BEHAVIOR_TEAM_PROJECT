
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import os
import seaborn as sns

dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = 'GatorCandy Case Data_Fall2021.sav'

data = pd.read_spss(dir_path+'/data_files/'+data_file)



df = data
#Question 1
def question_one(part):
    # whether we should care about employees' overall job satisfcation. Although a satisfied workforce is one of our 
    # strategic goals, we need to be sure, before we contemplate specific actions, that such actions are warranted Consider the following:

    #a. Does overall job satisfcation matter for work behaviors that we want to promote within the organization? Which Behaviors?
    #b. Does overall job satisfaction matter for work behaviors that we want to curb or eliminate within the organization? Which behaviors?
    q1_df = DataFrame([], columns=['Behavior', 'Correlation Value'])
    y = df['msq']

    if part.lower() == 'a':
        #MSQ is the Minnesota Satisfaction Questionaire. - Measure of overall job satisfaction
        behavior_list = ['agree', 'extra', 'open', 'conscin', 'neuro']
        for behavior in behavior_list:
            value_corr = y.corr(df[behavior])
            item = {'Behavior': behavior, 'Correlation Value': value_corr}
            q1_df = q1_df.append(item, ignore_index=True)
        print("Does overall job satisfcation matter for work behaviors that we want to promote within the organization? Which Behaviors? \n")
        return q1_df
        
    if part.lower() == 'b':
        behavior_list = ['OCB', 'Incivility', 'Cyberloafing']
        for behavior in behavior_list:
            value_corr = y.corr(df[behavior])
            item = {'Behavior': behavior, 'Correlation Value': value_corr}
            q1_df = q1_df.append(item, ignore_index=True)
        print("Does overall job satisfaction matter for work behaviors that we want to curb or eliminate within the organization? Which behaviors? \n")
        return q1_df
    else:
        print("you must select a or b")



print("question 1.a:")
print(question_one('a'))
print("\n")
print("question 1.b")
print(question_one('b'))




