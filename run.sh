#!/usr/bin/with-contenv bashio

python ./tpc-server.py $(bashio::services 'mqtt' 'host') $(bashio::services 'mqtt' 'username') $(bashio::services 'mqtt' 'password')
