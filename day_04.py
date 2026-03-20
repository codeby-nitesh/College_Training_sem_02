import pandas as pd
Data = {
    "Name":["Nitesh","Rahul","Lucky","Nadeem","Ritesh","Priyesh","Anuj","Ritesh"],
    "Branch":["B.Tech","B.Tech","B.Tech","B.Tech","BCA","BCA","BCA","BCA"],
    "Salary":[25000,23000,24000,23000,25000,26000,28000,96000,],
     "Age":[25,23,24,23,25,26,28,96],
    "Company Name":["Google","Google","Google","Google","Google","Google","Google","Google",],
    "Position":["Softwere Engineer","Web Developer","Management","Team Leader","CEO","Head of the management","Machin Engineer","Reader"]
}
df = pd.DataFrame(Data)
#print(df)
#df.to_csv('nitesh_data.csv')
#print(df[['Name','Salary']])
#print(df.loc[(df.Name == 'Nitesh')])

#print(df.loc[(df['Name'] == 'Nitesh') & (df['Salary'] <= 30000)])

#filtered = df[(df['Name'] == 'Nitesh') & (df['Salary'] >= 25000)]
#print(filtered)
# print((df.Salary >= 25000))

# print(df.iloc[0:5])

# df_Salary_filter = df[df['Salary']>=25000]
# print(df_Salary_filter)

# df_Salary_filter = df[(df['Salary'] >= 25000) & (df['Age']>=25)]

# print(df_Salary_filter)
# df_filter_ = df.where(df['Age'] >= 24 ,other = 'not eligible')
# print(df_filter_)


#Add new colum
# df['Team'] = ['CEO','HR','Accountent','Marketing','Boss','Developer','HR','Sales']
# print(df)

# df['Bonus'] = df['Salary']*0.3

# print(df)


# df['Bonus'] = df['Salary'] * 0.3
# df['Final Salary'] = df['Salary'] + df['Bonus']

# print(df)



df.loc[len(df)] = ['xyz','BBA',21000,36,'Deloite','Writer',]
#print(df)
df['Bonus'] = df['Salary'] * 0.3
df['Final Salary'] = df['Salary'] + df['Bonus']

#print(df)

df.loc[6,'Salary'] = 500000
# df.to_csv('update_nitesh_data.csv')
#print(df)

# remove = df.drop(df[df.Name == 'Ritesh'].index)


# update = df.drop('Bonus',axis = 1)
# print(update)

# print(df)


# update2 = df.drop('Bonus',exis=1,inplace=True)
# print(update2)



def calc(num1,num2):
    return num1+num2

calculation = calc(10,20)
print(calculation)

