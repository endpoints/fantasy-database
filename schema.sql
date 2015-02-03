CREATE TABLE authors (
  id integer PRIMARY KEY,
  name text NOT NULL CHECK(name <> ''),
  date_of_birth date NOT NULL,
  date_of_death date
);

CREATE TABLE series (
  id integer PRIMARY KEY,
  title text NOT NULL CHECK(title <> '')
);

CREATE TABLE books (
  id integer PRIMARY KEY,
  author_id integer NOT NULL REFERENCES authors(id),
  series_id integer REFERENCES series(id),
  date_published date NOT NULL,
  title text NOT NULL CHECK(title <> '')
);

CREATE TABLE chapters (
  id integer PRIMARY KEY,
  book_id integer NOT NULL REFERENCES books(id),
  title text NOT NULL CHECK(title <> ''),
  ordering integer NOT NULL
);

CREATE TABLE stores (
  id integer PRIMARY KEY,
  name text NOT NULL CHECK(name <> '')
);

CREATE TABLE books_stores (
  book_id integer NOT NULL REFERENCES books(id),
  store_id integer NOT NULL REFERENCES stores(id)
);
