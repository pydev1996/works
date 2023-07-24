from pyresparser import ResumeParser
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
def resume_scan(files,jd):
    #files=["Naveen.pdf","siva.pdf","Abhijeet.pdf","Robert.pdf","karthik.pdf"]
    name=[]
    mobile=[]
    mail=[]
    skills=[]
    resume_name=[]
    for f in files:
        data = ResumeParser(f).get_extracted_data()
        name.append(data['name'])
        mobile.append(data['mobile_number'])
        mail.append(data['email'])
        skills.append(data['skills'])
        resume_name.append(f.split("/")[-1])
    df=pd.DataFrame({"Name":name,"Email":mail,"Mobile":mobile,"Skills":skills,"FileName":resume_name})
    

    lmtzr = WordNetLemmatizer()
    df['Skills'] = df['Skills'].apply(lambda lst:[lmtzr.lemmatize(word) for word in lst])
    df['Skills']=[','.join(map(str,l)) for l in df['Skills']]
    skil_data=df['Skills'].to_numpy().tolist()
    jd1=lmtzr.lemmatize(jd)
    skil_data.insert(0,jd1)
    
    model2 = SentenceTransformer('stsb-bert-base')
    #Encoding:
    sen_embeddings2 = model2.encode(skil_data)
    
    f2=cosine_similarity(
        [sen_embeddings2[0]],
        sen_embeddings2[1:]
    )
    df['sbert_similarty']=f2[0]
  
    df1=df.loc[df['sbert_similarty']>0.4][['Name','Email','Mobile','FileName']]
    
    print("We Got "+str(len(df1.values.tolist()))+" Profiles:")
    
    df2 = df1.to_dict('records')
    for i in df2:
      print(i)
    if len(df1)>0:
        return df1
    else:
        return df[df['sbert_similarty']==df['sbert_similarty'].max()][['Name','Email','Mobile','FileName']]

#files=('E:/Resume _Screening/Abhijeet.pdf', 'E:/Resume _Screening/karthik.pdf', 'E:/Resume _Screening/Naveen.pdf', 'E:/Resume _Screening/Robert.pdf', 'E:/Resume _Screening/siva.pdf')
#jd='Java technologies,Good communication skills, both written and verbal'
#jd='python application'
#resume_scan(jd)