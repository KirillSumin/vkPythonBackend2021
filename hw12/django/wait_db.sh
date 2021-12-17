#!/bin/bash
while [[ $(curl --connect-timeout 2 -s -o /dev/null -w ''%{exitcode}'' $POSTGRES_SERVICE_NAME:$POSTGRES_PORT) == 7  ||  $(curl --connect-timeout 2 -s -o /dev/null -w ''%{http_code}'' $ELASTIC_SERVICE_NAME:$ELASTIC_PORT) != 200 ]]; 
    do 
        echo 'not yet'
        sleep 5
    done
echo 'db is up'