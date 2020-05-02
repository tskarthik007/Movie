#importing the lib
import pandas as pd
import pickle

#giving the names to the column names
# col_name=['user_id','item_id','rating','timestamp']

#were the file is stored(locally)
path="input/ratings.csv"

#reading the file using pandas
df=pd.read_csv(path)

#reading the movie file
movie_titles=pd.read_csv("input/movies.csv")
movie_titles['title']=movie_titles.title.str.slice(0,-7,None)

#merging the movie file and rating file using item_id
data=pd.merge(df,movie_titles,on='item_id')

#calculating the mean(rating ) for each movie
rating=pd.DataFrame(data.groupby('title')['rating'].mean())

rating['num of ratings']=pd.DataFrame(data.groupby('title')['rating'].count())

moviemat=data.pivot_table(index='user_id',columns='title',values='rating')

#input
#the movie name is give here for which the prediction is done
class predict():
    def pre(self,user):
        user=moviemat[user]

        #correlatin using pearson is used 
        similar=moviemat.corrwith(user,method="pearson")

        result=pd.DataFrame(similar,columns=['Correlation'])
        result=result.join(rating['num of ratings'])

        result=result[result['num of ratings']>100].sort_values('Correlation',ascending=False).head(6).reset_index()
        
        result=result.drop(['num of ratings','Correlation'],axis=1)
        result=result.drop([0])
        return result


result=predict()

pickle.dump(result,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))




