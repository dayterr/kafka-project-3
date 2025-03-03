команда для запуска

`docker compose up -d`

компоненты:
1. x-kafka-common – конфигурация кластера Kafka
2. postgres – экземпляр БД
3. kafka-0, kafka-1, kafka-2 – узлы кластера
4. schema-registry – управление схемами данных
5. ui – интерфейс пользователя для Kafka
6. connector – коннектор, который читает метрики из Kafka и по ручке /metrics отдаёт данные Prometheus в соответствующем формате
7. prometheus – инструмент сбора метрик

сценарий тестирования:
1. создать топик 'test', например, через kafka ui
2. положить в топик тестовое сообщение 
```
{
	"TestMetric": {
		"Type": "gauge",
		"Name": "TestMetric",
		"Description": "TestMetric is for testing.",
		"Value":1
	},
	"TestMetric2": {
		"Type": "gauge",
		"Name": "TestMetric2",
		"Description": "TestMetric2 is for testing.",
		"Value":1
	},
	"TestMetric3": {
		"Type": "gauge",
		"Name": "TestMetric3",
		"Description": "TestMetric3 is for testing.",
		"Value":1
	},
	"TestMetric4": {
		"Type": "gauge",
		"Name": "TestMetric4",
		"Description": "TestMetric4 is for testing.",
		"Value":1
	}
}
```
3. проверить, например, в Postman, что возвращает ручка (должна вернуть тестовое сообщение)
`localhost:8000/metrics`
4. положить в топик другое тестовое сообщение 
```
{
	"AnotherTestMetric": {
		"Type": "gauge",
		"Name": "TestMetric",
		"Description": "AnotherTestMetric is for testing.",
		"Value":3
	},
	"AnotherTestMetric2": {
		"Type": "gauge",
		"Name": "AnotherTestMetric2",
		"Description": "AnotherTestMetric2 is for testing.",
		"Value":3
	},
	"AnotherTestMetric3": {
		"Type": "gauge",
		"Name": "AnotherTestMetric3",
		"Description": "AnotherTestMetric3 is for testing.",
		"Value":3
	},
	"AnotherTestMetric4": {
		"Type": "gauge",
		"Name": "AnotherTestMetric4",
		"Description": "AnotherTestMetric4 is for testing.",
		"Value":3
	}
}
```
5. убедиться по той же ручке, что сообщение изменилось