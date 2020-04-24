#!/bin/bash

until bash -c "ssh -o StrictHostKeyChecking=no $PROD_SERVER 'docker ps'"; do
    >&2 echo "Server is not ready - sleeping"
    sleep 10
done

# Send Latest Scripts to Production Server
rsync -e "ssh -o StrictHostKeyChecking=no" -avz scripts/ $PROD_SERVER:/var/www/app/rolorex/scripts/
rsync -e "ssh -o StrictHostKeyChecking=no" -avz etc/ $PROD_SERVER:/var/www/app/rolorex/etc/
scp -o StrictHostKeyChecking=no docker-compose.yml $PROD_SERVER:/var/www/app/rolorex/docker-compose.yml

# Clean up old images
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'docker system prune --force --volumes'

# Log into Production Server, Pull and Restart Docker
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'cd /var/www/app/rolorex && docker-compose -p rolorex pull'
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'cd /var/www/app/rolorex && docker-compose -p rolorex build'
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'cd /var/www/app/rolorex && docker-compose -p rolorex up -d'
