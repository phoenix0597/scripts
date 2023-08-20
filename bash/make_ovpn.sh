#!/bin/bash

# Directory where EasyRSA outputs the client keys and certificates
KEY_DIR=~/clients/keys

# Where this script should create the OpenVPN client config files
OUTPUT_DIR=~/clients/files

# Base configuration for the client
BASE_CONFIG_FILE=~/clients/files/base.conf

client_id="client"

function main() {


read -p "Set client number (e.g. 1, 2 or 3 etc.): " client_number

if [ ! -z "${client_number}" ]; then
  client_id=${client_id}-${client_number}
fi


if [ ! -f ${BASE_CONFIG_FILE} ]; then
  echo "ERROR: Base configuration for the client ${BASE_CONFIG_FILE} not found"
  exit 1
fi

if [ ! -f ${KEY_DIR}/ca.crt ]; then
  echo "ERROR: CA certificate ${KEY_DIR}/ca.crt not found"
  exit 1
fi

if [ ! -f ${KEY_DIR}/${client_id}.crt ]; then
  echo "ERROR: User certificate ${KEY_DIR}/${client_id}.crt not found"
  exit 1
fi

if [ ! -f ${KEY_DIR}/${client_id}.key ]; then
  echo "ERROR: User private key ${KEY_DIR}/${client_id}.key ] not found"
  exit 1
fi

if [ ! -f ${KEY_DIR}/ta.key ]; then
  echo "ERROR: TLS Auth key not found"
  exit 1
fi

cat ${BASE_CONFIG_FILE} \
    <(echo -e '<ca>') \
    ${KEY_DIR}/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    ${KEY_DIR}/${client_id}.crt \
    <(echo -e '</cert>\n<key>') \
    ${KEY_DIR}/${client_id}.key \
    <(echo -e '</key>\n<tls-auth>') \
    ${KEY_DIR}/ta.key \
    <(echo -e '</tls-auth>') \
    > ${OUTPUT_DIR}/${client_id}.ovpn

echo "INFO: Key created in ${OUTPUT_DIR}/${client_id}.ovpn"

exit 0
}

# call main function
main 
