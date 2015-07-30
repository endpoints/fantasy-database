const Bookshelf = require('../');

module.exports = Bookshelf.Model.extend({
  tableName: 'photos',
  hasTimestamps: ['created_at', 'updated_at'],
  imageable: function () {
    return this.morphTo(
      'imageable',
      require('./author'),
      require('./series'),
      require('./book')
    );
  }
});
