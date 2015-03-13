const fs = require('fs');
const path = require('path');
const data = require('../data');
const schemaFile = path.join(__dirname, '..', 'schema.sql');
const schema = fs.readFileSync(schemaFile, 'utf-8');
const sqlite3 = require('sqlite3').verbose();

module.exports = function (file) {
  try { fs.unlinkSync(file); } catch (e) {}
  var db = new sqlite3.Database(file);
  db.serialize(function () {
    schema.split('\n\n').map(function (sql) {
      db.run(sql);
    });
    Object.keys(data).forEach(function (table) {
      var rows = data[table];
      rows.forEach(function (row) {
        var columns = Object.keys(row);
        var values = columns.map(function (column) { return row[column]; });
        var sql = [
        'INSERT INTO',
        table,
        '('+columns.join(',')+')',
        'VALUES',
        '(?'+new Array(columns.length).join(',?')+')'
        ].join(' ');
        db.run(sql, values);
      });
    });
  });
  db.close();
};
