import pickle
import os
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import pairwise

class language_detection:
    def __init__(self):
         #    ''' Constructor for this class. '''
         __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
         self.svd=pickle.load(open(__location__+"//data//svd.MODEL",'rb'))
         self.vocabulary=pickle.load(open(__location__+"//data//lexicon.MODEL",'rb'))
         self.id_of_languages=pickle.load(open(__location__+"//data//language_id.MODEL",'rb'))
         self.svdmatrix=pickle.load(open(__location__+"//data//svdmatrix.MODEL",'rb'))


    def lnaguage_list(self):
        lan_list=[]
        for item in self.id_of_languages.keys():
            lan_list.append((self.id_of_languages[item]['id'],self.id_of_languages[item]['name']))
        return lan_list

    def index_finder(self,text):
        clean_text=self.clean(text)
        n_gram=self.ngram_extractor(clean_text)
        matrix=self.ngram_to_matrix(n_gram)
        svd_matrix=self.svd_transform(matrix)
        index=self.detect_similarity(svd_matrix)
        return index

    def langauge_id(self,text):
        index=self.index_finder(text)
        print "The Language ID is: "+self.id_of_languages[index]["id"]
        return self.id_of_languages[index]["id"]

    def langauge_name(self,text):
        index=self.index_finder(text)
        print "The Language Name is: "+self.id_of_languages[index]["name"]
        return self.id_of_languages[index]["name"]


    def clean(self,text):
        try:
            clean_text=text.decode("utf8").lower()
        except:
            clean_text=text.lower()
        clean_text=clean_text.replace(" ","")
        return clean_text


    def ngram_extractor(self,text):
        n_gram_list=[]
        for i in range(len(text)-3):
            n_gram_list.append(text[i:i+4])
        return list(set(n_gram_list))

    def ngram_to_matrix(self,n_gram):
        matrix=[0]*len(self.vocabulary)
        for gram in n_gram:
            try:
                position=self.vocabulary[gram]
                matrix[position]=1
            except:
                pass
        return matrix

    def svd_transform(self,matrix):
        return self.svd.transform([matrix])


    def detect_similarity(self,svd_matrix):
        ind=0
        max_sim=-1
        sim=pairwise.cosine_similarity(self.svdmatrix,svd_matrix)
        for i in range(len(sim)):
            if(sim[i]>max_sim):
                max_sim=sim[i]
                ind=i
        return ind

