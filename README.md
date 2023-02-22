## How to start rabbitmq container:
* docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_VHOST=scraping -e RABBITMQ_DEFAULT_USER=fiitkar -e RABBITMQ_DEFAULT_PASS=123 -p 8080:15672 -p 5672:5672 rabbitmq:management-alpine

## What to do next
* You can load to admin console on http://localhost:8080 (username and password in settings.py - credentials in docker run cmd should match the ones in settings.py)
* After that run: python ./main.py
* The previous cmd starts program, which connects to rabbitmq container and creates test_consumer_queue and test_producer_queue (you can find them in admin console on tab queues)
* In RabbitMQ admin console go to queues tab
* Click on test_consumer_queue
* Click publish message
* In headers add: Content-Type=application/json
* In payload add example message from below

### Example output message
```
{
    "html": "<div><h1>Murder in Los Angels</h1><p>Elon Musk did blackmail. WTF man??. He might even do a burglary , who knows at this point...</p></div>",
    "original_crime": "Murder",
    "text": "Hola Mundo, Hola perros!",
    "language": "spa"
    "tags": {
        "LOC": {"Los Angels": 1}
        "PER": {"Elon Musk": 1}
        "ORG": {"WTF": 1}
        "MISC": {}
    }
}
```

doc: https://hub.docker.com/_/rabbitmq