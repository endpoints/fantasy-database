class Store < Sequel::Model
  many_to_many :books
end
