## [UDeltio](http://udeltio.com)

UDeltio is a bulletin board app for universities. It's name stands for University Bulletin (Deltio is Bulletin in Greek).

UDeltio provides an easy, effortless method for members of the university community to communicate with each other.

There are different __boards__ for various topics, members can create __posts__ on these boards.

The users have to be logged in to be able to access [UDeltio](http://udeltio.com) boardds. Once logged in, they can view the list of existing public boards on their home page. They can read and create posts in existing boards, or choose to start their own boards. A user may mark the board as favourite or remove it from favourites. 

Board owners can view and change settings of the board, such as board name, public / private status. They could also assign other users read / write / admin privileges with respect to the board, or change existing permissions. 

## The API

Our product uses a RESTful API written in Python using [Flask](http://flask.pocoo.org) allowing for a multitude of interactive frontends to be easily added. It also uses an OAuth like token based authentication system which allows for easy non-session based authentication. The API is documented using [API Blueprints](http://apiblueprint.org) and can be viewed through [Apiary.io](http://docs.udeltio.apiary.io)

## The Database

UDeltio uses [SQLAlchemy](http://www.sqlalchemy.org) as an [ORM](http://en.wikipedia.org/wiki/Object-relational_mapping) to interact with its database. Doing so allows the specific database to easily be changed without modification of the product. With this the specific database schema differs depending on the database that is attached, though we have described a [schema](DB Schema.png) using [mysql](https://www.mysql.com) types.

## The Web Frontend

The web frontend for UDeltio is built to work with our RESTful API. By using [Angular.js](https://angularjs.org) along with [Restangular](https://github.com/mgonto/restangular), we are able to leverage the power behind [MVC](http://en.wikipedia.org/wiki/Model–view–controller) to easily build a clean and coherent interface that is not hard tied into a model. This, along with the frontend interface being completely written in JavaScript, allows for an offline mode to be added to it later which can be useful for mobile users.
