лог из контейнера postgres (там коннектор)

```
2025-03-03 17:08:59 The files belonging to this database system will be owned by user "postgres".
2025-03-03 17:08:59 This user must also own the server process.
2025-03-03 17:08:59 
2025-03-03 17:08:59 The database cluster will be initialized with locale "en_US.utf8".
2025-03-03 17:08:59 The default database encoding has accordingly been set to "UTF8".
2025-03-03 17:08:59 The default text search configuration will be set to "english".
2025-03-03 17:08:59 
2025-03-03 17:08:59 Data page checksums are disabled.
2025-03-03 17:08:59 
2025-03-03 17:08:59 fixing permissions on existing directory /var/lib/postgresql/data ... ok
2025-03-03 17:08:59 creating subdirectories ... ok
2025-03-03 17:08:59 selecting dynamic shared memory implementation ... posix
2025-03-03 17:08:59 selecting default max_connections ... 100
2025-03-03 17:08:59 selecting default shared_buffers ... 128MB
2025-03-03 17:08:59 selecting default time zone ... Etc/UTC
2025-03-03 17:08:59 creating configuration files ... ok
2025-03-03 17:09:00 running bootstrap script ... ok
2025-03-03 17:09:01 performing post-bootstrap initialization ... ok
2025-03-03 17:09:01 syncing data to disk ... ok
2025-03-03 17:09:01 
2025-03-03 17:09:01 
2025-03-03 17:09:01 Success. You can now start the database server using:
2025-03-03 17:09:01 
2025-03-03 17:09:01     pg_ctl -D /var/lib/postgresql/data -l logfile start
2025-03-03 17:09:01 
2025-03-03 17:09:01 waiting for server to start....2025-03-03 14:09:01.571 GMT [48] LOG:  starting PostgreSQL 16.4 (Debian 16.4-1.pgdg110+2) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
2025-03-03 17:09:01 2025-03-03 14:09:01.573 GMT [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-03-03 17:09:01 2025-03-03 14:09:01.582 GMT [51] LOG:  database system was shut down at 2025-03-03 14:09:01 GMT
2025-03-03 17:09:01 2025-03-03 14:09:01.591 GMT [48] LOG:  database system is ready to accept connections
2025-03-03 17:09:01  done
2025-03-03 17:09:01 server started
2025-03-03 17:09:02 CREATE DATABASE
2025-03-03 17:09:02 
2025-03-03 17:09:02 
2025-03-03 17:09:02 /usr/local/bin/docker-entrypoint.sh: sourcing /docker-entrypoint-initdb.d/init-permissions.sh
2025-03-03 17:09:02 
2025-03-03 17:09:02 waiting for server to shut down....2025-03-03 14:09:02.110 GMT [48] LOG:  received fast shutdown request
2025-03-03 17:09:02 2025-03-03 14:09:02.112 GMT [48] LOG:  aborting any active transactions
2025-03-03 17:09:02 2025-03-03 14:09:02.138 GMT [48] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
2025-03-03 17:09:02 2025-03-03 14:09:02.139 GMT [49] LOG:  shutting down
2025-03-03 17:09:02 2025-03-03 14:09:02.142 GMT [49] LOG:  checkpoint starting: shutdown immediate
2025-03-03 17:09:02 2025-03-03 14:09:02.208 GMT [49] LOG:  checkpoint complete: wrote 922 buffers (5.6%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.032 s, sync=0.027 s, total=0.070 s; sync files=301, longest=0.008 s, average=0.001 s; distance=4249 kB, estimate=4249 kB; lsn=0/19D4A90, redo lsn=0/19D4A90
2025-03-03 17:09:02 2025-03-03 14:09:02.215 GMT [48] LOG:  database system is shut down
2025-03-03 17:09:02  done
2025-03-03 17:09:02 server stopped
2025-03-03 17:09:02 
2025-03-03 17:09:01 initdb: warning: enabling "trust" authentication for local connections
2025-03-03 17:09:01 initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
2025-03-03 17:09:02 2025-03-03 14:09:02.411 GMT [1] LOG:  starting PostgreSQL 16.4 (Debian 16.4-1.pgdg110+2) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
2025-03-03 17:09:02 2025-03-03 14:09:02.418 GMT [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2025-03-03 17:09:02 2025-03-03 14:09:02.418 GMT [1] LOG:  listening on IPv6 address "::", port 5432
2025-03-03 17:09:02 2025-03-03 14:09:02.422 GMT [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-03-03 17:09:02 2025-03-03 14:09:02.460 GMT [64] LOG:  database system was shut down at 2025-03-03 14:09:02 GMT
2025-03-03 17:09:02 2025-03-03 14:09:02.502 GMT [1] LOG:  database system is ready to accept connections
2025-03-03 17:09:58 2025-03-03 14:09:58.974 GMT [84] LOG:  logical decoding found consistent point at 0/1A3DAF8
2025-03-03 17:09:58 2025-03-03 14:09:58.974 GMT [84] DETAIL:  There are no running transactions.
2025-03-03 17:09:58 2025-03-03 14:09:58.974 GMT [84] STATEMENT:  CREATE_REPLICATION_SLOT "debezium"  LOGICAL decoderbufs
2025-03-03 17:09:58 2025-03-03 14:09:58.976 GMT [84] LOG:  exported logical decoding snapshot: "00000008-00000002-1" with 0 transaction IDs
2025-03-03 17:09:02 PostgreSQL init process complete; ready for start up.
2025-03-03 17:09:02 
2025-03-03 17:09:58 2025-03-03 14:09:58.976 GMT [84] STATEMENT:  CREATE_REPLICATION_SLOT "debezium"  LOGICAL decoderbufs
2025-03-03 17:09:59 2025-03-03 14:09:59.233 GMT [84] LOG:  starting logical decoding for slot "debezium"
2025-03-03 17:09:59 2025-03-03 14:09:59.233 GMT [84] DETAIL:  Streaming transactions committing after 0/1A3DB30, reading WAL from 0/1A3DAF8.
2025-03-03 17:09:59 2025-03-03 14:09:59.233 GMT [84] STATEMENT:  START_REPLICATION SLOT "debezium" LOGICAL 0/1A43498
2025-03-03 17:09:59 2025-03-03 14:09:59.234 GMT [84] LOG:  logical decoding found consistent point at 0/1A3DAF8
2025-03-03 17:09:59 2025-03-03 14:09:59.234 GMT [84] DETAIL:  There are no running transactions.
2025-03-03 17:09:59 2025-03-03 14:09:59.234 GMT [84] STATEMENT:  START_REPLICATION SLOT "debezium" LOGICAL 0/1A43498
```