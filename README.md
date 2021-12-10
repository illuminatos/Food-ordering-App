FOOD-ORDERING APP

MAIN COMPONENTS
    • Django → 3.2.9
    • Celery → 4.3.0
    • RabbitMq
    • Docker
    • Sqlite3
    • Swagger

URLs
    • /admin →  It can be added restaurant, categories and menu items as menu on related tabs. Also it can be added user details on user tab.
    • /order → it can be added order that post ingredient such like {“menu_items”: [2,3]} or {“menu_items”: [1]} take saved menu items id. Back-end can save order table in background.
    • /order-view-set → shows order detail.
    • /kindergarten → :D swagger api doc. It can be available whole api details. And also can be tried POST and GET methods to related api. 
    • /docs → It can be seen technical details about api like query parameters or response schema on this uri. 

WORKING PRINSIBLE

/order api takes detail about order and saved on DB as state waiting. After that celery task run and publish data to RabbitMq. Subscriber takes data from RabbitMq and subscribe service process data and update state of data Aproved. Then it can be seen on /order-view-set api.

RUN as A CONTAINER

After pull project, in order of these command → with sudo docker-compose build and sudo docker-compose up, run project as a container. 
On a terminal 
    • sudo docker ps shows running containers. There are named as 2 backend-image (one api and other is worker as a consumer) and rabbitmq:3-management 
    • sudo docker container logs -f <container id>  → shows logs
    • sudo docker container exec -it <container-id> /bin/bash → get inside container

RUN ON LOCAL IDE

    • Check rabbitmq status → sudo systemctl status rabbitmq-server

    • if not run, start rabbitmq on your local with command → sudo systemctl start rabbitmq-server
    • on your ide local terminal → python manage.py runserver → as api
    • on your ide second local terminal → celery -A food_ordering worker –loglevel=INFO → run as a worker
TEST
    • run → python manage.py test
      

