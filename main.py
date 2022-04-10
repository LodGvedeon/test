from pydantic.main import BaseModel
import requests


class Post(BaseModel):
    """
    Base Post Model
    """
    userId: int
    id: int
    title: str
    body: str
    
    def print_post_body(self):
        print(self.body)
    
    def print_info(self):

        print('User Id is: ', self.userId)
        print('Post Id is: ', self.id)
        print('Post Title is: ', self.title)
        print('Post Body is: ', self.body)
            
print('Script starting')
resp = requests.get(
    'https://jsonplaceholder.typicode.com/posts/1'
)
data_raw = resp.json()
post_new = Post(**data_raw)
post_new.print_info()

