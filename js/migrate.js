const path = require('path');
const fs = require('fs');

const dbFile = path.join(__dirname, '..', 'fantasy.db');
const schemaFile = path.join(__dirname, '..', 'schema.sql');
const dataFile = path.join(__dirname, '..', 'data');

try {
  fs.unlinkSync(dbFile);
} catch (e) {}

const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database(dbFile);

const schema = fs.readFileSync(schemaFile, 'utf-8');
const data = require(dataFile);

console.log('creating database...');
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
console.log('done.')
