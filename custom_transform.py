def custom_transform(df):
    df= df.copy()
    df['Family'] = df['SibSp'] + df['Parch']
    df=df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin','SibSp','Parch'], axis=1)
    return df