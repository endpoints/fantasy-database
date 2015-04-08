class Series < Sequel::Model
  one_to_many :books
  one_to_many :photo, :as => :imageable
end
