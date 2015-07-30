const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'authors',
  hasTimestamps: ['created_at', 'updated_at'],
  books: function () {
    return this.hasMany(require('./book'));
  },
  photos: function () {
    return this.morphMany(require('./photo'), 'imageable');
  }
});
