Эксперимент	batch.size	linger.ms	compression.type	buffer.memory	Source Record Write Rate (kops/sec)
1	500	1000	none	33554432	1.87
2   100	0	    none	33554432	0.544
3	500	1000	snappy	33554432	1.15
4	1000 1000	none	33554432	3.29
5	1000 2000	none	33554432	6.33

увеличение параметров batch.size и linger.ms даёт прирост в скорости записи, однако нужно учитывать, что могут тратиться ресурсы кластера.

как проверить:
1. в папке /kafka-project-3/part1/grafana/dashboards лежит файл connect.json, его нужно подгрузить в Grafana, если он окажется не подгружен при запуске.
2. создать таблицу people, команда:
```
CREATE TABLE IF NOT EXISTS people (
 id int PRIMARY KEY,
 name varchar(255),
 private_info VARCHAR,  
 updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
3. выставить нужные настройки конфига коннектора, например (curl-команду также легко использовать в postman):
```
curl --location --request PUT 'http://localhost:8083/connectors/postgres-source/config' \
--header 'Content-Type: application/json' \
--data '{
"connector.class":"io.confluent.connect.jdbc.JdbcSourceConnector",
"tasks.max":"1",
"connection.url":"jdbc:postgresql://postgres:5432/customers?user=postgres-user&password=postgres-pw&useSSL=false",
"connection.attempts":"5",
"connection.backoff.ms":"50000",
"mode":"timestamp",
"timestamp.column.name":"updated_at",
"topic.prefix":"postgresql-jdbc-bulk-",
"table.whitelist": "people",
"poll.interval.ms": "200",
"batch.max.rows": 100,
"producer.override.linger.ms": 2000,
"producer.override.batch.size": 1000,
"compression.type": "none",
"transforms":"MaskField",
"transforms.MaskField.type":"org.apache.kafka.connect.transforms.MaskField$Value",
"transforms.MaskField.fields":"private_info",
"transforms.MaskField.replacement":"CENSORED"
}'
```
4. данные для тестов:
```
INSERT INTO people (id, name, private_info)
SELECT
   i,
  'Name_' || i || '_' || substring('abcdefghijklmnopqrstuvwxyz', (random() * 26)::integer + 1, 1),
 'Private_info_' || i || '_' || substring('abcdefghijklmnopqrstuvwxyz', (random() * 26)::integer + 1, 1)
FROM
   generate_series(1, 9000000) AS i;
```

