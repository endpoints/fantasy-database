const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'stores',
  hasTimestamps: ['created_at', 'updated_at'],
  books: function () {
    return this.belongsToMany(require('./book'));
  }
});
