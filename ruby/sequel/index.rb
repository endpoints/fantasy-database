$LOAD_PATH.unshift File.expand_path(File.dirname(__FILE__))

require 'sequel'

DB = Sequel.connect('sqlite://fantasy.db')

require 'models/author'
require 'models/book'
require 'models/chapter'
require 'models/series'
require 'models/store'
