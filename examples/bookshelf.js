const fantasyDatabase = require('../js'); // require('fantasyDatabase');
const BookshelfModels = require('../js/bookshelf'); // require('fantasyDatabase/js/bookshelf');

// Provide your own Knex connection
const Knex = require('knex')({
  client: 'sqlite3',
  debug: false,
  connection: {
    // this builds a fresh sqlite3 database at the provided file location
    filename: fantasyDatabase(__dirname+'/fantasy.db')
  }
});

// Provide your own Bookshelf
const Bookshelf = require('bookshelf')(Knex);

// Use the model objects in this repo to make model instances
const models = Object.keys(BookshelfModels).reduce(function (result, modelName) {
  var model = BookshelfModels[modelName];
  result[model] = Bookshelf.Model.extend(model.instanceProps, model.classProps);
  return result;
}, {});

// Fetch data from the database!
models.authors.collection().fetch().then(function (authors) {
  console.log(authors);
});
