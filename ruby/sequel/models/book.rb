class Book < Sequel::Model
  many_to_one :author
  many_to_one :series
  one_to_many :photos, :as => :imageable
end
