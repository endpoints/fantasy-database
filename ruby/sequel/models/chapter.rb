class Chapter < Sequel::Model
  many_to_one :book
end
