class Book < Sequel::Model
  many_to_one :author
  many_to_one :series
end
