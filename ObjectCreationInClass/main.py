from PreprocesssText import PreprocesssText

if __name__ == '__main__':
    
    
    text = '''For me the love should start with attraction.si should feel that I need her every time around me.
              she should be the first thing which comes in my thoughts.I would start the day and end it with her.she should be there every time I dream.love will be then when my every breath has her name.my life should happen around her.my life will be named to her.I would cry for her.will give all my happiness and take all her sorrows.I will be ready to fight with anyone for her.I will be in love when I will be doing the craziest things for her.love will be when I don't have to proove anyone that my girl is the most beautiful lady on the whole planet.I will always be singing praises for her.love will be when I start up making chicken curry and end up makiing sambar.life will be the most beautiful then.will get every morning and thank god for the day because she is with me.I would like to say a lot..will tell later'''
    obj = PreprocesssText()
    tokenwords = obj.token_words(text)
    print(tokenwords)
    
    
    
    

