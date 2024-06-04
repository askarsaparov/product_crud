# Product CRUD with elastic search

## Running the Setup
`docker-compose up`

## Create Super User
`docker-compose exec web python manage.py migrate`

## Create Super User
`docker-compose exec web python manage.py createsuperuser`

## For Elasticsearch 
`docker-compose exec web python manage.py search_index --rebuild`
