from fastapi import status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session


def create_comment(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)


def delete_blog(id: int, response: Response, db: Session):
    # There are three options to delete records below

    # First, querying the record and set it to an instance
    # Then deleting the instance using db.delete method

    blog_detail = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_detail:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'There is no record with id {id}'}
    title = blog_detail.title
    db.delete(blog_detail)

    # Second, querying the record and set it to an instance
    # Then deleting the instance using instance's delete method

    # blog_detail = db.query(models.Blog).filter(models.Blog.id == id)
    #
    # if not blog_detail.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'Blog with id {id} not found')
    #
    # blog_detail.delete(synchronize_session=False)

    # Third, querying the record and deleting directly the instance in one line

    # blogs = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)

    # Due to autocommit option is False, we require using db.commit method
    db.commit()
    return {'detail': f'Blog id {id} ({title}) has been deleted successfully'}


def update(id: int, request: schemas.Blog, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'There is no record with id {id}'}

    blog.update(request.dict())
    db.commit()

    return {'detail': f'Blog id {id} has been updated successfully'}


def get_all_records(response: Response, db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'There is no record yet'}
    return blogs


def get_records_by_id(id, response: Response, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found')
    return blogs