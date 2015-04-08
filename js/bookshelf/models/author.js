const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'authors',
  books: function () {
    return this.hasMany(require('./book'));
  },
  photos: function () {
    return this.morphMany(require('./photo'), 'imageable');
  }
});
