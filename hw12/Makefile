build:
	sudo chmod -R 775 ../
	sudo docker-compose build

up:build
	sudo docker-compose up -d
	sudo docker-compose exec django bash ./wait_db.sh

migrate:up
	sudo docker-compose exec django python3 ./manage.py migrate

createsuper:migrate
	sudo docker-compose exec django python3 ./manage.py createsuperuser

stop:
	sudo docker-compose stop

clear:
	sudo docker-compose down
