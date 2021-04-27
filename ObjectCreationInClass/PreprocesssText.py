import string
from nltk.corpus import stopwords

class PreprocesssText(object):
    def ___init__(self):
        pass
    
    def remove_punctuations(self,text):
        '''Takes string and returns string'''
        return ''.join([x for x in text if x not in string.punctuation])
    
    def remove_stopwords(self,text):
        
        # split the text
        # lower case the words
        # consider if word not in stopword
        
        return ([x for x in text.split() if x.lower() not in stopwords.words('english')])
    
    def token_words(self,text=''):
        
        """
        Takes String
        Return Token also called  list of words that is used to 
        Train the Model 
        """
        
        message = self.remove_punctuations(text)
        words = self.remove_stopwords(message)
        return words