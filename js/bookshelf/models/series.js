const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'series',
  books: function () {
    return this.hasMany(require('./book'));
  }
});
