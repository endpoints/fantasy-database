const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'series',
  hasTimestamps: ['created_at', 'updated_at'],
  books: function () {
    return this.hasMany(require('./book'));
  },
  photo: function () {
    return this.morphOne(require('./photo'), 'imageable');
  }
});
