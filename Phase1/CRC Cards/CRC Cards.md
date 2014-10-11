#### User

| Responsibilities | Collaborators |
|------------------|---------------|
knows username     | 
has a first name   | 
has a last name    |


#### Board

| Responsibilities | Collaborators |
|------------------|---------------|
has an identifier  | User
knows users who are subscribed to it | Post
knows tags that are assigned to it | Tag
knows whether it is public or private | 


#### Post

| Responsibilities | Collaborators |
|------------------|---------------|
Has an identifier  | User
knows its posting user | Board
Knows the board it belongs to | 
Knows its posting time |
knows its subject |
Knows its content |
Knows whether it is important or not |


#### Tag

| Responsibilities | Collaborators |
|------------------|---------------|
Has an identifier |
Has a display title |


#### UserDAO

| Responsibilities | Collaborators |
|------------------|---------------|
Create user with given username and password | User
Get a user, given correct username/password pair |


#### PostDAO

| Responsibilities | Collaborators |
|------------------|---------------|
Create a post on a board, given board id, user id, and post content | Post
Update a post given post id | 
Retrieve a post given post id |
Delete a post using post id and user id |
Get all posts by user, given username |


#### BoardDAO

| Responsibilities | Collaborators |
|------------------|---------------|
Create a board given user id | Board
Retrieve a board given a board id | Tag
Get all posts in a board given a board id |
Delete a board given a board id and user id |
Retrieve users who can read posts in board given user id |
Retrieve users who can create posts in board given user id and post | 
Retrieve users who can administer the board given user id | 
Retrieve all boards assigned a tag given tag id |
Subscribe a user to a board given username and board id |
Unsubscribe a user from the board given username and board id |


#### CachingDAO

| Responsibilities | Collaborators |
|------------------|---------------|
takes a instance of a class which implements a DAO | DAO
overrides the DAO's get method to lazily call database |