import sqlite3
from models import Post_Reaction

def create_post_reaction(new_post_reaction):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO PostReactions
            ( reaction_id, user_id, post_id )
        VALUES
            ( ?, ?, ?);
        """, (new_post_reaction['reaction_id'], new_post_reaction['user_id'], new_post_reaction['post_id']), )
        
        id = db_cursor.lastrowid
        new_post_reaction['id'] = id
      
    return new_post_reaction

def delete_post_reaction(id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM PostReactions
        WHERE id = ?
        """, (id, ))

def get_reactions_of_post(post_id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
        *
        FROM PostReactions p
        WHERE p.post_id = ?
        """, (post_id, ))
        
        reactions = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            reaction = Post_Reaction(row['id'], row['reaction_id'], row['user_id'], row['post_id'])

            reactions.append(reaction.__dict__)

    return reactions

def get_users_reactions_of_post(post_id, user_id):
    with sqlite3.connect("./db.sqlite3") as conn:
      
        print(post_id), print(user_id)
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT *
        FROM PostReactions p
        WHERE p.post_id = ? AND p.user_id = ?
        """, (post_id, user_id))
        
        reactions = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            reaction = Post_Reaction(row['id'], row['reaction_id'], row['user_id'], row['post_id'])

            reactions.append(reaction.__dict__)

    return reactions