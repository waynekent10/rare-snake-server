from models import Tag
import sqlite3

def create_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label)
        VALUES
            (?);
        """, (new_tag['label'],))

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return new_tag

def get_all_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
        *
        FROM Tags t
        """)
        
        tags = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

    return tags

def get_single_tag(tag_id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT *
        FROM Tags t
        WHERE t.id = ?
        """, (tag_id, ))
                
        data = db_cursor.fetchone()
        
        tag = Tag(data['id'], data['label'])

    return tag.__dict__

def delete_tag(id):
        with sqlite3.connect('./db.sqlite3') as conn:
            db_cursor = conn.cursor()
            db_cursor.execute("""
            DELETE FROM Tags
            WHERE id = ?
            """, (id,))