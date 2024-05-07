import sqlite3
from models import PostTag

def create_post_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO PostTags
            ( post_id, tag_id )
        VALUES 
            ( ?, ? );
        """, (new_tag['post_id'], new_tag['tag_id']), )
        
        id = db_cursor.lastrowid
        new_tag['id'] = id
    return new_tag

def delete_post_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, (id, ))

def get_posts_by_tags(tag_id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTags pt
        WHERE pt.tag_id = ?
        """, (tag_id, ))

        post_tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])
            post_tags.append(post_tag.__dict__)

    return post_tags
