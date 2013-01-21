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



misc references
---------------

http://blog.garrypolley.com/

https://github.com/loku/heroku-buildpack-multi (didn't use)


actually working
----------------

back to jiaaro

add /app/bin to PATH (via config:add)
add /app/lib/python2.7/site-packages to PYTHONPATH

default PATH is /app/.heroku/python/bin:/usr/local/bin:/usr/bin:/bin
default PYTHONPATH is /app/

jiaaro PATH is /usr/local/bin:/usr/bin:/bin
jiaaro PYTHONPATH is nothing


and here's what to set with heroku config:add

new PATH is /app/bin:/app/.heroku/python/bin:/usr/local/bin:/usr/bin:/bin
new PYTHONPATH is /app:/app/lib/python2.7/site-packages:/app/lib/python2.7:/app/lib




S3
--

`django-storage` docs: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html


