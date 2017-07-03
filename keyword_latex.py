from urllib.parse import quote

def keyword_latex(Input):
    query = "https://latex.codecogs.com/gif.latex?%5Cbg_white&space;"+quote(Input)
    return(query)    
