import sqlite3
import json
from datetime import datetime
from models import User

# login user function was created for us in the user.py file
def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True and the user's id as the token
                     If the user was not found will return valid boolean False
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)

# get users
def get_all_users():
    with sqlite3.connect("./db.sqlite3") as conn:

      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
          u.id,
          u.first_name,
          u.last_name,
          u.email,
          u.bio,
          u.username,
          u.password,
          u.profile_image_url,
          u.created_on,
          u. active
      FROM users u
      """)

      users = []

      dataset = db_cursor.fetchall()

      for row in dataset:

          user = User(row['id'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])

          users.append(user.__dict__)

    return users

# get single user
def get_single_user(id):
    with sqlite3.connect("./db.sqlite3") as conn:

      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
          u.id,
          u.first_name,
          u.last_name,
          u.email,
          u.bio,
          u.username,
          u.password,
          u.profile_image_url,
          u.created_on,
          u. active
      FROM users u
      WHERE u.id = ?
      """, ( id, ))

      data = db_cursor.fetchone()

      user = User(data['id'], data['first_name'], data['last_name'], data['email'], data['bio'], data['username'], data['password'], data['profile_image_url'], data['created_on'], data['active'])

      return user.__dict__

# create user ( there is a create user function in the user.py file)
def create_user(user):
    """Adds a user to the database when they register

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    try:
        with sqlite3.connect("./db.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO users (first_name, last_name, username, email, password, bio, created_on, active)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                user['first_name'],
                user['last_name'],
                user['username'],
                user['email'],
                user['password'],
                user['bio'],
                datetime.now()
            ))

            id = db_cursor.lastrowid

            return json.dumps({
                'token': id,
                'valid': True
            })
    except Exception as e:
        print("Error:", e)
        return json.dumps({
            'error': str(e),
            'valid': False
        })
      
# update user
def update_user(id, new_user):
      with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE users
            SET
                first_name = ?,
                last_name = ?,
                email = ?,
                bio = ?,
                username = ?,
                password = ?,
                profile_image_url = ?,
                created_on = ?,
                active = ?
        WHERE id = ?
        """, (new_user['first_name'], new_user['last_name'], new_user['email'], new_user['bio'], new_user['username'], new_user['password'], new_user['profile_image_url'], new_user['created_on'], new_user['active'], id, ))
        
# test for delete, although we may not want to delete a user in FE.
def delete_user(id):
        with sqlite3.connect("./db.sqlite3") as conn:
            db_cursor = conn.cursor()
            db_cursor.execute("""
            DELETE FROM users
            WHERE id = ?
            """, (id,))

# alter get user and get single user to also get associated posts?
