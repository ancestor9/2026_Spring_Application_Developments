from pydantic import BaseModel

class Who(BaseModel):
    who: str
    
def post_hi(item: Who):
    return {"message": f"Hello {item.who}!"}

item = Who(who="Alice")
response = post_hi(item)    
print(response.text)  # Output: {'message': 'Hello Alice!'}  