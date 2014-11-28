# Architecture
Our system incorporated two main components a RESTful API and a Javascript web client. We chose to build our system in this way because we knew that having a RESTful API for all of our data access would allow easier addition of additional new clients.

## Backend
The RESTful API was implemented in Python using the [Flask framework](http://flask.pocoo.org). This allowed us to implement the system using MVC patterns by providing easy ways to split the model and controller. We also used the [SQLAlchemy](http://www.sqlalchemy.org) [ORM](http://en.wikipedia.org/wiki/Object-relational_mapping) to abstract away the database interactions and to provide a clean Python interface to our data. This also allows us to easily change database technologies without changing our implementation.

![Database Schema](../DB Schema.png)

## Frontend
We used [Angular.js](https://angularjs.org) to implement the front end of UDeltio. Angular separates views and controllers which made it easier for us to distribute the work among team members. We had the following controllers for the front end:
* Main controller
* Board controller
* Menu controller
* Profile controller
The Main controller took care of the routing to different urls of the website, while the other controllers were responsible for their respective entities.

As an interface to the RESTful API on the backend, we used [Restangular](https://github.com/mgonto/restangular) on the frontend as a layer of abstraction for the requests we were making.

We relied heavily upon existing open source library for the front end.
* Angular [Route](https://docs.angularjs.org/api/ngRoute/service/$route), to help with the routing in the Main controller
* [Bootstrap](http://getbootstrap.com) library to make front end development easier
* [Angular-Bootstrap](https://github.com/angular-ui/bootstrap) to tie Angular directives to Bootstrap components
* [Marked.js](https://github.com/chjj/marked) to process HTML rendering of the posts entered using Markdown syntax
* [Typeahead.js](https://twitter.github.io/typeahead.js/) and ng-tags-input directive, to make adding tags to the boards easier and to enable auto-completion of existing tags.

The reasoning behind using these pre-existing libraries was to increase our development speed, to come up with a feature rich product in a short time period.
