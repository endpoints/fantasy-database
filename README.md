# fantasy-database
> A database with a few fantasy books in it for testing query builders, orms, rest frameworks, etc.

### How does it work?
The schema is defined in [schema.sql](https://github.com/endpoints/fantasy-database/blob/master/schema.sql) using MySQL compatible syntax (bleh) because SQLite doesn't seem to recognize PostgreSQL's `serial` datatype and won't auto-increment IDs when used. The seed data is defined in [data.json](https://github.com/endpoints/fantasy-database/blob/master/data.json).

If you are a node user, running `npm install && npm start` will rebuild the SQLite database file (which is checked into the root of this repository as [fantasy.db](https://github.com/endpoints/fantasy-database/blob/master/data.json)).

### How do I use it?
Make this repository a dependency of your project and automate the process of copying `fantasy.db` into your testing harness.

Because this repository is meant to be used by multiple programming languages, there are no affordances for auto-migrating your database (PRs welcome!). Use [schema.sql](https://github.com/endpoints/fantasy-database/blob/master/schema.sql) as a reference for building migrations, and [data.json](https://github.com/endpoints/fantasy-database/blob/master/data.json) for seeding if you'd like to test in something other than SQLite.

#### Usage notes
- [Python](python)
