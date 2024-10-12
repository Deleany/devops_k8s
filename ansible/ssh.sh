#!/usr/bin/bash

HOST_KEY_NAME="ansible_ssh_key"
USER="root"
PASS="CHANGE_ME_PLS"

echo $HOST_KEY_NAME
echo $USER
echo $PASS

dnf install sshpass -y

echo "start to gen ssh key"
ssh-keygen -t ed25519 -b 2048 -f /root/.ssh/$HOST_KEY_NAME -C ansible_host -q -N ""

echo 'start to add key go ssh-agent'
ssh-add /root/.ssh/$HOST_KEY_NAME



echo "start to key propagation"
for server in $(cat /etc/ansible/hosts | tail -n +2); \
do sshpass -p "$PASS" ssh-copy-id -i /root/.ssh/"$HOST_KEY_NAME".pub $USER@"$server"; \
done

echo "DONE!"