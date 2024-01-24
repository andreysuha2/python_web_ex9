class AuthorUrlsStore:
    __instance = None
    
    def __init__(self):
        self.urls = set()
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(AuthorUrlsStore)
        return cls.__instance
    
    def add(self, url):
        self.urls.add(url)
        
authors_urls = AuthorUrlsStore()          
