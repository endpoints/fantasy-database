const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'chapters',
  hasTimestamps: ['created_at', 'updated_at'],
  book: function () {
    return this.belongsTo(require('./book'));
  }
});
