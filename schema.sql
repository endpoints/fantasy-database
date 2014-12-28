CREATE TABLE authors (
  id serial PRIMARY KEY,
  name text NOT NULL CHECK(name <> ''),
  date_of_birth date NOT NULL,
  date_of_death date
);

CREATE TABLE series (
  id serial PRIMARY KEY,
  title text NOT NULL CHECK(title <> '')
);

CREATE TABLE books (
  id serial PRIMARY KEY,
  author_id int NOT NULL REFERENCES authors(id),
  series_id int REFERENCES series(id),
  date_published date NOT NULL,
  title text NOT NULL CHECK(title <> '')
);

CREATE TABLE chapters (
  id serial PRIMARY KEY,
  book_id int NOT NULL REFERENCES books(id),
  title text NOT NULL CHECK(title <> ''),
  ordering int NOT NULL
);
