exports.instanceProps = {
  tableName: 'series',
  books: function () {
    return this.hasMany(require('./books'));
  }
};

exports.classProps = {
  typeName: 'series',
  fields: [
    'id',
    'title'
  ],
  filters: {
    title: function (qb, value) {
      return qb.whereIn('title', value);
    }
  },
  relations: [
    'books'
  ]
};
