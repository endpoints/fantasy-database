
# fantasy-database

> A database with a few fantasy books in it for testing query builders, orms, rest frameworks, etc.


## Django

This test app for Django provides models, migrations, and fixtures that implement the fantasy-database. It's
recommended that app installation be limited to testing only.

Example usage:

In your `settings.py` module:

```python

# Testing
TESTING = len(sys.argv) > 1 and sys.argv[1] in ('test', 'testserver')

if TESTING:
    INSTALLED_APPS += (
        'django_fantasy',
    )

...
```

In a test module:
```python

from django.test import TestCase

class FantasyTests(TestCase):
    fixtures = ['fantasy-database.json']
    ...

```
