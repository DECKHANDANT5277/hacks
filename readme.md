# ```$_Hacks```
(still in development)
<br/>
dead simple but flexible restful api framework, <br/>
~~ for modern back-end web development of your dreams <br/>
<hr/>

## $ Features
### Restful api all the things !
1. [what is rest ?](http://www.restapitutorial.com/lessons/whatisrest.html)
2. **how hacks do ?** <br>
each time you run ***hack generate -api resources***, this is going to implement a full crud restful api for resources as well as search and pagination stuff!
thanks to [pony orm](https://github.com/ponyorm/pony) flexible [**Set** syntax](https://docs.ponyorm.com/relationships.html), you can easily add [one-to-many(many-to-many) relationships](https://docs.ponyorm.com/relationships.html) and hacks will **automatically generate relationship apis between resources**!

### Real time back-end service via socketIO
hacks apps are capable of full-duplex realtime communication between the client
and the server using [socketIO](http://socket.io/).  this means that a client
can maintain a persistent connection to a hacks backend service,  and messages
can be sent from client to server (AJAX) or from server to client (websocket) at any time.
<br/>
+ on server side, hacks integrate [flask-socketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
+ and on front-end, hacks use [jinja2](https://github.com/pallets/jinja) template that binding socketio service

### Flexible api configuration
+ hacks automatically generate resources apis, but you can get complete control by editing apis configuration. you can decide which data **user should post from** or **return as json format**; you can also determine which api **user can access** and set up your own **authentication policy**!

### Hacking on top of flask
+ [flask](http://flask.pocoo.org/) is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. <br/>
well, hacks is built on top of flask! so feel free to use any great flask extensions !

### Great DRY idea
+ hacks based on [DRY idea](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Since I do not want repeat myself, and try to sum up python web development procedure, so hacks appeared!
+ not only that, hacks use the DRY idea for web development, hacks has several useful built-in decorators help you reduce duplication. yes, decorators is awesome!

<hr>
## $ Get Start
### New a project
<code>$ hack new demo</code>

### Generate restful api
<code>$ hack generate -api users</code>

### Videos
+ [hacks framework](https://www.youtube.com/watch?v=aimpIJjk824)

<hr>

## $ Notes
Currently, Hacks simply generate a **prototype api**, which means the api **did
not** have:

1. **authentication mechanism**
2. **relationship between each api resource**,
3. **rate limit**
4. **http caching**
5. **user side config**
6. **invoke your own code**

and obviously, it ***not ready to go into production***;
<hr/>
But, I will continue to feed more on Hacks, and finally let Hacks become a
**production-oriented**  but **deadly simple** restful api framework.

<hr>
## $ Todo
+ [x] integrated the [pony orm](https://github.com/ponyorm/pony)
+ [ ] find a database schema migration tool
+ [ ] refactory hacks project
    + [x] basic example
        + [x] apis
        + [x] apps
+ [x] add resources model mixin class
+ [ ] binding socketio
    + [ ] server-side socketio: flask-socketIO
    + [ ] client-side jinja2 template
+ [ ] build api resources relationship
+ [ ] configurations
    + [ ] restful api config
    + [ ] resource bp config
    + [ ] authentication policy
+ [ ] front-end workflow
+ [ ] add mongodb layer

<hr>
## $ LICENSE
MIT, check LICENSE file for detail
