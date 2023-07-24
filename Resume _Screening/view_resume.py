from pyresparser import ResumeParser
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
def view(files):
    
    name=[]
    mobile=[]
    mail=[]
    skills=[]
    for f in files:
        data = ResumeParser(f).get_extracted_data()
        name.append(data['name'])
        mobile.append(data['mobile_number'])
        mail.append(data['email'])
        skills.append(data['skills'])
    df=pd.DataFrame({"Name":name,"Email":mail,"Mobile":mobile,"Skills":skills})
    #print(df.values.tolist()[0][0])
    return df
#files=["Naveen.pdf"]
#view(files)