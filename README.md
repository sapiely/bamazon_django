# Bamazon Django Browser application and RESTFULL API

## Instaling
    pip install -r requirements.txt

## Usage
    python manage.py runserver

## In browser:

#### Index/Books page.
    127.0.0.1:8000/
    
#### Django-admin page.
    127.0.0.1:8000/admin
     
#### List of all books in the store.
    127.0.0.1:8000/books
    
#### Page of a certain book by id.
    127.0.0.1:8000/books/<int:book_id>/
     
#### List of all authors in the store.
    127.0.0.1:8000/authors/
    
#### Page of a certain author by id.
    127.0.0.1:8000/authors/<int:author_id)>

## To use by REST API:

#### Get all books
    URL: http://{{server_url}}/api/books/
    METHOD: GET
    
    return: JSON of all books in the store.
    
#### Get a certain book
    URL: http://{{server_url}}/api/books/<int:book_id>/
    METHOD: GET
    
    return: JSON of a certain book by id.
    
#### Get all authors
    URL: http://{{server_url}}/api/authors/
    METHOD: GET
    
    return: JSON of all authors in the store.
    
#### Get a certain author
    URL: http://{{server_url}}/api/authors/<int:author_id>/
    METHOD: GET
    
    return: JSON of certain author by id.
