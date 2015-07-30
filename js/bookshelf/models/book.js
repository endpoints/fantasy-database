const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'books',
  hasTimestamps: ['created_at', 'updated_at'],
  author: function () {
    return this.belongsTo(require('./author'));
  },
  series: function () {
    return this.belongsTo(require('./series'));
  },
  photo: function () {
    return this.morphMany(require('./photo'), 'imageable', 'Book');
  }
});
