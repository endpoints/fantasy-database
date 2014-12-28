class Series < Sequel::Model
  one_to_many :books
end
