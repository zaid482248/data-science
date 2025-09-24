import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt 


df = pd.read_csv("D:\\Data Science\\data\\Project_Data\\mymoviedb.csv",engine="python" , on_bad_lines="skip" )

# Dalete Extra column 
columns = ["Overview" , "Original_Language" , "Poster_Url"]
df.drop(columns = columns ,axis= 1 , inplace= True)


df["Release_Date"] = pd.to_datetime(df["Release_Date"] , errors="coerce" , format= "mixed")
df["Release_Date"] = df["Release_Date"].dt.year 

# df["Vote_Count"] = df["Vote_Count"].fillna(0).astype(int)
# df["Vote_Average"] = df["Vote_Average"].fillna(0).astype(float)

df["Vote_Count"] = pd.to_numeric(df["Vote_Count"] , errors="coerce")
df["Vote_Average"] = pd.to_numeric(df["Vote_Average"] , errors= "coerce")




def categorize_column(df , col , labels):

    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max'],
             ]
    df[col] = pd.cut(df[col] , edges , labels=labels , duplicates= 'drop' )
    return df


label = ['not_Populer' , 'below_aga', 'average' , 'populer']

categorize_column(df , 'Vote_Average' , label)

# print(df["Vote_Average"].unique())
# print(df["Vote_Average"].value_counts())
# print(df.isna().sum())
# print(df.dropna(inplace=True))

# print(df.isna().sum())
df.dropna(inplace=True)  

df["Genre"] = df["Genre"].str.split(', ')
df = df.explode('Genre').reset_index(drop = True)

df["Genre"] = df["Genre"].astype("category")
# print(df["Genre"].dtypes)


sns.set_style('whitegrid')
# print(df["Genre"].describe())
# sns.catplot( y= 'Genre' , data= df , kind= 'count', order=df["Genre"].value_counts().index , color="#B82AA5")
# plt.title("Genre column distribution")
# plt.show()


# sns.catplot(y="Vote_Average" , data = df , kind= "count" ,order= df["Vote_Average"].value_counts().index ,color="#90268A" )
# plt.title("Movies Vote average")
# plt.show()

# print(df[df["Popularity"] == df["Popularity"].max()])
# print(df[df["Popularity"] == df["Popularity"].min()])
df["Year"] = df["Release_Date"]

# sns.catplot(x="Year"  ,data= df , kind="count" ,height= 6 , aspect= 2  )
df["Year"].hist()
plt.title("Movies data")
plt.xticks (rotation = 45   )
plt.show()











# print(df["Release_Date"].dtypes)
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.nunique())



# print(df.head(10))
