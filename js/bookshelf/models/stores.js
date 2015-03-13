exports.instanceProps = {
  tableName: 'stores',
  books: function () {
    return this.belongsToMany(require('./books'));
  }
};

exports.classProps = {
  typeName: 'stores',
  fields: [
    'id',
    'name'
  ],
  filters: {},
  relations: [
    'books'
  ]
};
