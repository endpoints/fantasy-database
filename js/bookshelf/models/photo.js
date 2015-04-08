const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'photos',
  imageable: function () {
    return this.morphTo(
      'imageable',
      require('./author'),
      require('./series'),
      require('./book')
    );
  }
});
