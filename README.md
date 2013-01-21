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


