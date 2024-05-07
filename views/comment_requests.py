import sqlite3
from models import Post

def get_comments_of_user(id):
    pass

def create_comment(new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( author_id, post_id, content )
        VALUES
            ( ?, ?, ?);
        """, (new_comment['author_id'], new_comment['post_id'],
              new_comment['content'], ))
        
        id = db_cursor.lastrowid
        new_comment['id'] = id
        
    return new_comment



