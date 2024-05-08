-- CREATE TABLE "Users" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "first_name" varchar,
--   "last_name" varchar,
--   "email" varchar,
--   "bio" varchar,
--   "username" varchar,
--   "password" varchar,
--   "profile_image_url" varchar,
--   "created_on" date,
--   "active" bit
-- );

-- CREATE TABLE "DemotionQueue" (
--   "action" varchar,
--   "admin_id" INTEGER,
--   "approver_one_id" INTEGER,
--   FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
--   FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
--   PRIMARY KEY (action, admin_id, approver_one_id)
-- );


-- CREATE TABLE "Subscriptions" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "follower_id" INTEGER,
--   "author_id" INTEGER,
--   "created_on" date,
--   FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
--   FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
-- );


-- CREATE TABLE "Posts" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "user_id" INTEGER,
--   "category_id" INTEGER,
--   "title" varchar,
--   "publication_date" date,
--   "image_url" varchar,
--   "content" varchar,
--   FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
-- );

-- CREATE TABLE "Comments" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "post_id" INTEGER,
--   "author_id" INTEGER,
--   "content" varchar,
--   FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
--   FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
-- );

-- -- CREATE TABLE "Reactions" (
-- --   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
-- --   "label" varchar,
-- --   "image_url" varchar
-- -- );

-- CREATE TABLE "PostReactions" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "user_id" INTEGER,
--   "reaction_id" INTEGER,
--   "post_id" INTEGER,
--   FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
--   FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
--   FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
-- );

-- CREATE TABLE "Tags" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "label" varchar
-- );

-- CREATE TABLE "PostTags" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "post_id" INTEGER,
--   "tag_id" INTEGER,
--   FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
--   FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
-- );

-- CREATE TABLE "Categories" (
--   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
--   "label" varchar
-- );

-- INSERT INTO Categories ('label') VALUES ('News');
-- INSERT INTO Tags ('label') VALUES ('JavaScript');
-- INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

-- INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content') VALUES (
-- '1', '1', 'My First Post', 20240506, 'https://pngtree.com/so/happy', 'i hope this works'
-- )
-- INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content') VALUES (
-- '2', '2', 'My Second Post', 20240507, 'https://pngtree.com/so/happy', 'this one is from the future'
-- )
-- INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content') VALUES (
-- '1', '3', 'My Third Post', 20240505, 'https://pngtree.com/so/happy', 'this one is from the past'
-- )

-- DELETE FROM Comments WHERE post_id = 1;
