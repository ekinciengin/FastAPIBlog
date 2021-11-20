from fastapi import APIRouter, Depends, status, Response
from typing import List
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_comment(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_comment(request, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, response, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, response, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def get_all_records(response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all_records(response, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_records_by_id(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_records_by_id(id, response, db)
