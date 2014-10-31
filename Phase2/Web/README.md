##Dev Environment Setup Instructions

###Python

- I highly suggest creating a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for the project, so you won't mess up your system python libraries.
- Install the requirements with [pip](https://pip.readthedocs.org/). `pip install -r requirements.txt`

###Node / Bower

- We use [npm](https://www.npmjs.org/) and [bower](http://bower.io/) for dependency management. Install nodejs and npm.

- Use `npm install` to setup the dependencies for development.
- You can also use `npm start` to start the development server. `npm start` will automatically run `npm install` each time.
    - If you're having issues with `npm start`, use `./udeltio` to start the development server.