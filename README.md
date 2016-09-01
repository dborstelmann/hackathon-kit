Hackathon Kit &mdash; and so much more
===========
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Ready made to be an instant project kit with almost no setup and is easily deployed

#### The stack is made up of the following:

- PostgreSQL
- Django
    - Models
    - Views
    - Auth (including already built `login`, `logout`, and `register` views)
- jQuery
- Underscore
    - Templates
- Backbone
    - Models and Collections
    - Views
- Materialize (easily swappable to bootstrap if you prefer)
- Less
    - less.js compiles in the browser, this is not recommended for production environments

## Local Setup

Please fork this repository and clone it to your computer so you can use it as the base for your project.

### 1. PostgreSQL

The first thing to do is make sure you have [PostgreSQL](https://www.postgresql.org/) downloaded, installed, and **running**.  Then either get [Postico](https://eggerapps.at/postico/ "A fantastic PostgreSQL application for Mac") or open a `psql` shell.

**Run the following commands:**

```
CREATE USER <your_username> WITH CREATEDB;
ALTER USER <your_username> WITH PASSWORD '<your_password>';
CREATE DATABASE <your_database> WITH OWNER <your_username>;
```

Now you should have a development database setup on your local machine for the app to use.

### 2. Django

**Run the following from your project directory in your shell:**

```
pip install -r requirements.txt
```

Next we need to set the following variables in our bash shell so that Django knows which database to use.

**Run the following in your shell:**

```
export HACKATHON_KIT_LOCAL_NAME=<your_database>
export HACKATHON_KIT_LOCAL_USERNAME=<your_username>
export HACKATHON_KIT_LOCAL_PASSWORD=<your_password>
export DJANGO_HACKATHON_KIT_SECRET_KEY="random_string_here"
```

> Note: If you don't want to have to set these variables every time you open a shell, you can set them in your .bashrc (or .zshrc like me), you can write a script to export them for you, or if you use a virtual environment (recommended) follow these [instructions](#additional-notes) to have the variables always exist when in your environment.

Then we need to bring your database up to date with the state of your models.

**Run the following from your project directory in your shell:**

```
python manage.py makemigrations
python manage.py migrate
```

**All that is left is to start your server and you will have a fully working full stack web application:**

```
python manage.py runserver
```

That is all you need to get started, however I have added sections below on the one-button install to [Heroku](https://www.heroku.com/) and an explanation of the frontend stack.


## Deploying to Heroku

This project is already set up to be immediately deployed to **Heroku** through one click of the following button.  All you have to do is add a name.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you want to change the settings of this deployment, please visit [app.json](./app.json)

- It comes standard with:
    - Free server
    - Free postgres database
    - Papertrail
        - Free app that allows you to view server logs easily

Once deployed on Heroku, you will want to download the [heroku toolbelt](https://devcenter.heroku.com/articles/heroku-command-line) to your local system.

Then **run the below command** to connect your local git repo with your Heroku instance, replacing `PROJECTNAME` with the name you set on your Heroku app when you deployed it.

```
heroku git:remote -a PROJECTNAME
```

Every time you push code to the Heroku server, **run the following from your project directory:**

```
git push heroku master
```

For more information on deploying with git to Heroku, look here: [Heroku: Deploying with Git](https://devcenter.heroku.com/articles/git)


## Frontend Stack

**There are two main goals for the frontend stack of this kit**

1. **Clean, organized, and modular code that can be easily reused.**
2. **Only the stuff you need for the page you are on, no big build files that make page loads slow.**

All of the frontend code is stored in the `webapp` folder.  Inside this you will find the `static` folder and the `templates` folder.  Let's start with the `static` folder.

- `dependencies`
    - All the frontend dependencies you would expect
        - jQuery
        - Underscore
        - Backbone
        - less.js (less compiler in the browser)
        - Materialize (`materialize.min.css` and `materialize.min.js`)
            - While it says they are minified, if you open the actual file you will see this is untrue.  This is for easier development, please minify before pushing to production.
- `js`
    - Stores any Backbone views, models, and collections files
    - Also where general app code goes. For example, there is already a `base.js` file which has a few utility functions and template settings for Underscore (mustache or handlebars style), and an app namespace.  Here is `base.js`

        ```javascript
        hk = {};
        BB = Backbone;

        _.templateSettings = {
            evaluate: /\{\{#(.+?)\}\}/g,
            interpolate: /\{\{=(.+?)\}\}/g,
            escape: /\{\{(?!#|=)(.+?)\}\}/g
        };

        // Usage (in your Underscore template): {{hk.underscorePartial('your-template-selector', templateScopedData)}}
        hk.underscorePartial = function (templateSelector, data) {
            return _.template($('#' + templateSelector).html())(data);
        };

        hk.checkForEnter = function (e) {
            if (e.which == 13 && !e.shiftKey) {
                e.preventDefault();
                $(e.target).blur();
            }
        };
        ```
- `less`
    - `base.less` is where your general app classes and variables would go (feel free to make as many of these files as you want for different parts of your app to make sure you are only loading what you need)
        - I have included a set of color variables for white, gray, and black, as well as some custom classes and an app font to get you started
    - All your other less files will import `base.less` or whatever file you choose to serve that purpose.  You can see this in `hello.less`

Now let's look at the `templates` folder.  Anything at the top level in this folder would be a page in your app (an html file you return from a Django view).

- The `base` folder
    - `links.html` has a list of the core dependencies needed on all pages (this includes any standard `js` files you want app-wide, Google Fonts, and Google Material Icons)
    - The `less_headers` folder
        - This is where you decide which less files get loaded for each page you return from a Django view, here is an example from `hello_less.html` (This file gets linked in the page's html file.)

            ```html
            {% load staticfiles %}
            <link type="text/css" rel="stylesheet/less" href="{% static "less/base.less" %}"/>
            <link type="text/css" rel="stylesheet/less" href="{% static "less/hello.less" %}"/>
            <script src="{% static "dependencies/less.min.js" type="text/javascript" %}"></script>
            ```
            > Note: This is where less.js compiles all of your less into css.  Any links to less files lower than this line on your html page will not compile or run.

- The `partials` folder
    - This folder is used to store all of the templates for your pages
    - I recommend making a subfolder for each page in your app as you can see I have done with `hello`
    - These files will be imported into script tags in your page's html to be used as Underscore templates.
    - Here is an example from `hello_base.html` (the verbatim tags are to leave the scope of the Django template language and enter the scope of the Underscore template language):

        ```html
        {% verbatim %}
        <div class="row">
            <div class="col s12">
                Your custom content.
            </div>
        </div>
        {% endverbatim %}
        ```

#### An example html file returned by a Django view

```html
<!doctype html>

<head>
    {% load staticfiles %}
    {% include "base/links.html" %}
    {% include "base/less_headers/hello_less.html" %}
</head>

<script id="hello-template" type="text/template">
    {% include "partials/hello/hello_base.html" %}
</script>

<body>
    <div id="hello">

    </div>
</body>

<script type="text/javascript" src="{% static "js/hello.js" %}"></script>
<script type="text/javascript">
    var helloView = new hk.HelloView();
</script>

</html>
```
- You can see all of the imports we talked about above (links, less headers, and an example template that will be used in our Backbone view)
- A `body` and page level `div` for your Backbone view to render it's content in
- The import for your Backbone code for this specific page
- The initialization of your Backbone view for this page

#### An example Backbone view

```javascript
hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    events: {
    },
});
```
> Note: The template is grabbed out of the script tag using jQuery and then turned into an Underscore template to be rendered

## Additional Notes

The immediate value of [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) is easily separating the `pip` installed requirements for different projects. Different problems call for different tools, many of which often conflict, and if you are working on a Hackathon you want as few tools affecting your code as possible in order to prevent unexpected errors.

More power comes from the virtualenvwrapper in its `postactivate` & `predeactivate` files. You can run code and make changes to your environment and variables every time you enter a virtual environment, and then revert the changes when you leave. These are things that you should get familiar with before you enter a competition in order to make your time more development and less set-up!

Below are handy scripts to load and unload the environment variables for your hackathon kit.

edit: `~/.virtualenvs/<virtual_env_name>/bin/postactivate`
```
#!/bin/zsh
# This hook is sourced after this virtualenv is activated.
export HACKATHON_KIT_LOCAL_NAME=<your_database>
export HACKATHON_KIT_LOCAL_USERNAME=<your_username>
export HACKATHON_KIT_LOCAL_PASSWORD=<your_password>
export DJANGO_HACKATHON_KIT_SECRET_KEY="random_string_here"
echo "Hackathon kit local variables have been set."
```

edit: `~/.virtualenvs/<virtual_env_name>/bin/predeactivate`
```
#!/bin/zsh
# This hook is sourced after this virtualenv is activated.
unset HACKATHON_KIT_LOCAL_NAME
unset HACKATHON_KIT_LOCAL_USERNAME
unset HACKATHON_KIT_LOCAL_PASSWORD
unset DJANGO_HACKATHON_KIT_SECRET_KEY
echo "Hackathon kit local variables removed."
```


## Author Note

Released by [Dan Borstelmann](https://github.com/dborstelmann) on August 29, 2016.
