class Photo < Sequel::Model
  many_to_one :imageable, :polymorphic => true
end
