const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'books',
  author: function () {
    return this.belongsTo(require('./author'));
  },
  series: function () {
    return this.belongsTo(require('./series'));
  }
});
