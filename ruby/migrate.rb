class CreateFantasy < ActiveRecord::Migration[5.1]
  def change
    create_table :authors do |t|
      t.text :name, null: false
      t.date :date_of_birth, null: false
      t.date :date_of_death

      t.timestamps
    end

    create_table :photos do |t|
      t.text :title, null: false
      t.text :uri, null: false
      t.references :imageable, polymorphic: true

      t.timestamps
    end

    create_table :series do |t|
      t.text :title
      t.references :photo, foreign_key: true

      t.timestamps
    end

    create_table :books do |t|
      t.text :title, null: false
      t.date :date_published, null: false
      t.references :author, foreign_key: true
      t.references :series, foreign_key: true

      t.timestamps
    end

    create_table :chapters do |t|
      t.text :title, null: false
      t.integer :ordering, null: false
      t.references :book, foreign_key: true

      t.timestamps
    end

    create_table :stores do |t|
      t.text :name, null: false

      t.timestamps
    end

    create_table :books_stores, id: false do |t|
      t.belongs_to :book, index: true
      t.belongs_to :store, index: true
    end
  end
end
