from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = { 
    1: {"title": "Hello World"  }, 
    2: {"title": "Understanding FastAPI Basics" }, 
    3: {"title": "Dependency Injection Explained" }, 
    4: {"title": "Working with Pydantic Models" }, 
    5: {"title": "Async Database Access Patterns" }, 
    6: {"title": "Building RESTful Endpoints" }, 
    7: {"title": "Error Handling Best Practices" }, 
    8: {"title": "Testing FastAPI Apps" }, 
    9: {"title": "Deploying to Production" }, 
    10:{"title": "Performance Tuning Tips" }
}

@app.get("/posts")
def get_all_posts(limit: int):
    if limit:
        return {k: text_posts[k] for k in list(text_posts)[:limit]}
    return text_posts

@app.get("/posts/{id}", response_model=PostResponse)
def get_post(id : int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    post = text_posts.get(id)
    return PostResponse(id=id, title=post["title"])

@app.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate) -> PostResponse:
    if post.id in text_posts:
        raise HTTPException(status_code=400, detail="Post ID already exists")
    text_posts[post.id] = {"title": post.title}
    return PostResponse(id=post.id, title=post.title)

@app.delete("/posts/{id}")
def delete_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    del text_posts[id]
    return {"detail": "Post deleted successfully"}
