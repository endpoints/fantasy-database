const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'stores',
  books: function () {
    return this.belongsToMany(require('./book'));
  }
});
