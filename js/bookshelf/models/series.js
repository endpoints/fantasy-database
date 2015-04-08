const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'series',
  books: function () {
    return this.hasMany(require('./book'));
  },
  photo: function () {
    return this.morphOne(require('./photo'), 'imageable');
  }
});
