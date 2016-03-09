$ docker-compose up -d
Creating salt_master_1
Creating salt_minion_1

$ docker exec -ti salt_master_1 salt \* test.ping
6725d7c3f253:
    True

$ docker-compose scale minion=5
Creating and starting 2 ... done
Creating and starting 3 ... done
Creating and starting 4 ... done
Creating and starting 5 ... done

$ docker exec -ti salt_master_1 salt \* test.ping
ee26d4e3699d:
    True
41794f7494cf:
    True
2ef93c536c21:
    True
6725d7c3f253:
    True
3a632c95fb3c:
    True

$ docker-compose ps
    Name                 Command            State                                    Ports
---------------------------------------------------------------------------------------------------------------------------
salt_master_1   /usr/local/bin/entrypoint   Up      0.0.0.0:4505->4505/tcp, 0.0.0.0:4506->4506/tcp, 0.0.0.0:32774->8000/tcp
salt_minion_1   /usr/local/bin/entrypoint   Up      4505/tcp, 4506/tcp, 8000/tcp
salt_minion_2   /usr/local/bin/entrypoint   Up      4505/tcp, 4506/tcp, 8000/tcp
salt_minion_3   /usr/local/bin/entrypoint   Up      4505/tcp, 4506/tcp, 8000/tcp
salt_minion_4   /usr/local/bin/entrypoint   Up      4505/tcp, 4506/tcp, 8000/tcp
salt_minion_5   /usr/local/bin/entrypoint   Up      4505/tcp, 4506/tcp, 8000/tcp
