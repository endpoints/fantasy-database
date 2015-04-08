class Author < Sequel::Model
  one_to_many :books
  one_to_many :photos, :as => :imageable
end
