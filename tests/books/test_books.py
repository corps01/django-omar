# from unicodedata import name
# import pytest
# from library.books.models import *

# # @pytest.mark.django_db
# # def test_author_name():
# #   author = Author.objects.create(name='Paulo',last_name='Coelho')
# #   print('This is my authors name: ', author.name)
# #   assert author.last_name == 'Coelho'
# #   assert Author.objects.all().count()==1

# # @pytest.mark.django_db
# # def test_genre_name():
# #   genre = Genre.objects.create(name='Action')
# #   print('This is my genre name: ', genre.name)
# #   assert genre.name == 'Action'
# #   genre = Genre.objects.create(name='Adventure')
# #   assert Genre.objects.all().count()==2


# @pytest.mark.django_db
# @pytest.mark.parametrize(
# 	'val',
# 	(
# 	'Action',
#     'Adventure',
#     'Mystery'
# 	)
# )

# def test_genre_name(val):
#   genre = Genre.objects.create(name=val)
#   print('This is my genre name: ', genre.name)
#   assert genre.name == val

# # ####

# @pytest.mark.django_db
# @pytest.mark.parametrize(
# 	'val',
# 	(
# 	'Action',
#     'Adventure',
#     'Mystery'
# 	)
# )

# def test_genre_type(val):
#   genre = Genre.objects.create(name=val)
#   print('This are my genres: ', genre.name)
#   assert type(genre.name) == str

# @pytest.mark.django_db
# @pytest.mark.parametrize(
# 	'val1, val2',
# 	(
# 		('CoMEdy', 'Comedy'),
#     ('HoRrOr', 'Horror'),
#     ('FanTasy', 'Fantasy')
# 	)
# )

# def test_genre_capitalize_name(val1,val2):
#   genre = Genre.objects.create(name=val2)
#   print('This is my genre name: ', genre.name)
#   assert genre.name != val1

# @pytest.mark.django_db
# @pytest.mark.parametrize(
# 	'val',
# 	(
# 	'Action',
#     'Adventure',
#     'Mystery'
# 	)
# )

# def test_genre_leng(val):
#   genre = Genre.objects.create(name=val)
#   print('This are my genres: ', genre.name)
#   assert len(genre.name) <= 128

# #########

# @pytest.fixture
# def fixture_genre_create():
#     genre = Genre.objects.create(name='Test')
#     return genre

# @pytest.mark.django_db
# def test_genre_delete(fixture_genre_create):
#     amount = fixture_genre_create
#     print('genre created')
#     amount.delete()
#     print('genre deleted')
#     assert Genre.objects.count() == 0

# ########

# @pytest.mark.django_db
# @pytest.mark.parametrize(
# 	'lang',
# 	(
# 	'Spanish',
#     'English',
#     'Russian'
# 	)
# )

# def test_language_type(lang):
#   language = Language.objects.create(name=lang)
#   print('Theese are language: ', language.name)
#   assert type(language.name) == str


# ########

# @pytest.mark.django_db
# @pytest.mark.parametrize(
# 	'lan1, lan2',
# 	(
# 		('Spanish', 'sPanish'),
#     ('English', 'englIsh'),
#     ('Russian', 'rusSSian')
# 	)
# )
# def test_language_format(lan1,lan2):
#   genre = Genre.objects.create(name=lan2)
#   print('This is my genre name: ', genre.name)
#   assert genre.name != lan1

# @pytest.mark.django_db
# def test_author_with_monkey(monkeypatch):
#   author = Author.objects.create(name='name',last_name='apellido')
  
#   def model_count_mock():
#     return 4
  
#   print(dir(Author.objects))
#   print(type(Author.objects))
#   print(type(Author.objects.all()))
#   monkeypatch.setattr(Author.objects, 'count', model_count_mock)

#   assert Author.objects.count()==4
#   print('Haciendo el monkeypatch')