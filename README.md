three-little-birds
==================

Website for the Three Little Birds


Environment variables to configure on Heroku:
S3 stuff
`DEBUG=False`
^^ that one's IMPORTANT


Use a custom buildpack so we can use lessc and coffeescript:

```sh
heroku config:add BUILDPACK_URL=git://github.com/jiaaro/heroku-buildpack-django.git
```
so far the custom buildpack is not working...
... switched back to heroku's


-----------------

back to jiaaro

add /app/bin to PATH (via config:add)
add /app/lib/python2.7/site-packages to PYTHONPATH

default PATH is 
default PYTHONPATH is

new PATH is /usr/local/bin:/usr/bin:/bin:/app/bin
new PYTHONPATH is /app/lib/python2.7/site-packages
