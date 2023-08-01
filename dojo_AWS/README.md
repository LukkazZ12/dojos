# dojo-AWS
Dojo de AWS, DynamoDB na 42sp

Como configurar

Dentro da pasta configure deste repositorio, rode 

docker-compose up

para descobrir o id do container, rode 

docker ps

O primeiro numero da resposta e o id desse container, agora rode esse comando com o id que pegou

docker exec -it {CONTAINER_ID} /bin/bash

Agora voce esta dentro do container em que vamos rodar tudo
