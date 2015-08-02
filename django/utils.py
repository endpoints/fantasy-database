
from datetime import datetime
from django.utils import timezone


def translate_fixture(data):
    """
    Translate the contents of the `data.json` file into a django compatible fixture.
    """
    results = []
    now = datetime.now().replace(tzinfo=timezone.UTC()).isoformat()

    for author in data['authors']:
        results.append({
            'pk': author['id'], 'model': 'fantasy.author',
            'fields': {
                'created_at': now,
                'updated_at': now,
                'name': author['name'],
                'date_of_birth': author['date_of_birth'],
                'date_of_death': author['date_of_death'],
            }
        })

    for series in data['series']:
        results.append({
            'pk': series['id'], 'model': 'fantasy.series',
            'fields': {
                'created_at': now,
                'updated_at': now,
                'title': series['title'],
            }
        })

    for book in data['books']:
        results.append({
            'pk': book['id'], 'model': 'fantasy.book',
            'fields': {
                'created_at': now,
                'updated_at': now,
                'series': book['series_id'],
                'author': book['author_id'],
                'title': book['title'],
                'date_published': book['date_published'],
            }
        })

    for chapter in data['chapters']:
        results.append({
            'pk': chapter['id'], 'model': 'fantasy.chapter',
            'fields': {
                'created_at': now,
                'updated_at': now,
                'title': chapter['title'],
                'book': chapter['book_id'],
                'ordering': chapter['ordering'],
            }
        })

    for store in data['stores']:
        results.append({
            'pk': store['id'], 'model': 'fantasy.store',
            'fields': {
                'created_at': now,
                'updated_at': now,
                'name': store['name'],
                'books': [sb['book_id'] for sb in data['books_stores'] if sb['store_id'] == store['id']],
            }
        })

    for photo in data['photos']:
        types_map = {
            'authors': ('fantasy', 'author'),
            'books': ('fantasy', 'book'),
            'series': ('fantasy', 'series'),
        }

        results.append({
            'pk': photo['id'], 'model': 'fantasy.photo',
            'fields': {
                'created_at': now,
                'updated_at': now,
                'imageable_id': photo['imageable_id'],
                'imageable_type': types_map[photo['imageable_type']],
                'title': photo['title'],
                'uri': photo['uri'],
            }
        })

    return results
