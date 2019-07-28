class Source:
    '''
    class source retrieves the news source
    '''

    def __init__(self,id,name):
        self.id =id
        self.name = name
        
class Article:
    
    """ class article gives more insights on the news stories """
    
    def  __init__(self, author ,title, description, url, urlToImage , publishedAt, content ):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    