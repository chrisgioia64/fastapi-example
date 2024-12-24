from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    content: str

posts = []

@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    posts.append(post)
    return post

@app.get("/posts/", response_model=List[Post])
def get_posts():
    return posts

@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, updated_post: Post):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}", response_model=Post)
def delete_post(post_id: int):
    for index, post in enumerate(posts):
        if post.id == post_id:
            deleted_post = posts.pop(index)
            return deleted_post
    raise HTTPException(status_code=404, detail="Post not found")