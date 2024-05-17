import sqlite3
from models import Post

def get_all_posts():
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content
        FROM Posts p
        """)
        
        posts = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'])

            posts.append(post.__dict__)

    return posts

def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content
        FROM Posts p
        WHERE p.id = ?
        """, (id, ))
                
        data = db_cursor.fetchone()
            
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'], data['publication_date'], data['image_url'], data['content'])

    return post.__dict__

def create_post(new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content )
        VALUES
            ( ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content']), )
        
        id = db_cursor.lastrowid
        new_post['id'] = id
      
    return new_post
        
def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))
        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE post_id = ?
        """, (id, ))
        

def update_post(id, new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?
        WHERE id = ?
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], id, ))
        
        rows_affected = db_cursor.rowcount
        
    if rows_affected == 0:
        return False
    else:
        return True

def get_posts_by_user(user_id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content
        FROM Posts p
        WHERE p.user_id = ?
        """, (user_id, ))
        
        posts = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'])

            posts.append(post.__dict__)
    return posts
