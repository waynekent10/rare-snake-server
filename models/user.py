class User():
  
    def __init__(self, id, first_name, last_name, email, bio, username, password, profile_image_url, created_on, active):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.username = username
        self.password = password
        self.profile_image_url = profile_image_url
        self.created_on = created_on
        self.active = active
        
    def no_show_password(self):
      return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "email": self.email,
        "bio": self.email,
        "username": self.username,
        "profile_image_url": self.profile_image_url,
        "created_on": self.created_on,
        "active": self.active
      }
