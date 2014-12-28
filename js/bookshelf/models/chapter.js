const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'chapters',
  book: function () {
    return this.belongsTo(require('./book'));
  }
});
