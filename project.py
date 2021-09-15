#%%
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import os
import seaborn as sns
from scipy.stats import ttest_1samp, ttest_ind

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


def question_two(part):

    headers = ['overall', 'pay','work',' coworkers','supervision','promotions','salary','merit']

    benchmark_data_mean = [74.72, 59.05, 37.19, 38.61, 39.58, 7.45, 70523, 3500]
    benchmark_data_stdv = [10.49, 12.52, 11.72, 12.37, 10.01, 14.43, 30597, 541]
    benchmark_data_sample = [395, 250, 400, 400, 370, 440, 1250, 1250]

    if part.lower() == 'a':
        
        avg_overall_satisfaction = df['msq'].mean()
        avg_pay_satisfaction = df['psq'].mean()
        avg_satisfaction_work = df['jdiw'].mean()
        avg_satisfaction_cowork = df['jdic'].mean()
        avg_satisfaction_super = df['jdis'].mean()
        avg_satisfaction_promo_oppo = df['jdipro'].mean()
        avg_salary = df['salary'].mean()
        avg_merit = df['merit'].mean()

        ttest_overall_satisfaction = ttest_1samp(df['msq'], benchmark_data_mean[0])
        ttest_pay_satisfaction = ttest_1samp(df['psq'], benchmark_data_mean[1])
        ttest_satisfaction_work = ttest_1samp(df['jdiw'], benchmark_data_mean[2])
        ttest_satisfaction_cowork = ttest_1samp(df['jdic'], benchmark_data_mean[3])
        ttest_satisfaction_super = ttest_1samp(df['jdis'], benchmark_data_mean[4])
        ttest_satisfaction_promo_oppo = ttest_1samp(df['jdipro'], benchmark_data_mean[5])
        ttest_salary = ttest_1samp(df['salary'], benchmark_data_mean[6])
        ttest_merit = ttest_1samp(df['merit'], benchmark_data_mean[7])

        ttest_list = [ttest_overall_satisfaction[0], ttest_pay_satisfaction[0], ttest_satisfaction_work[0], 
                      ttest_satisfaction_cowork[0], ttest_satisfaction_super[0], ttest_satisfaction_promo_oppo[0],
                      ttest_salary[0], ttest_merit[0]]

        pvalue_list = [ttest_overall_satisfaction[1], ttest_pay_satisfaction[1], ttest_satisfaction_work[1], 
                      ttest_satisfaction_cowork[1], ttest_satisfaction_super[1], ttest_satisfaction_promo_oppo[1],
                      ttest_salary[1], ttest_merit[1]]

        avg_list = [avg_overall_satisfaction, avg_pay_satisfaction, avg_satisfaction_work, 
                    avg_satisfaction_cowork, avg_satisfaction_super, avg_satisfaction_promo_oppo, avg_salary, avg_merit]

        # print(ttest_list)
        # print(pvalue_list)
        for i in range(len(avg_list)):
            print(headers[i])
            print('gator: '+str(avg_list[i]), 'benchmark: '+str(benchmark_data_mean[i]), 'p-score: '+str(pvalue_list[i]))
            if avg_list[i] < benchmark_data_mean[i]:
                print("lower! \n")
            else:
                print("higher \n")


        
        #part a
        # we are lower in everything except  for 

        return 
        

# print("question 1.a:")
# print(question_one('a'))
# print("\n")
# print("question 1.b")
# print(question_one('b'))

print(question_two('a'))




