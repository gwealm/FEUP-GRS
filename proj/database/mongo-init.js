// Connect to the admin database
db = db.getSiblingDB('admin');

// Authenticate using environment variables
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);

// Switch to the default database
db = db.getSiblingDB(process.env.MONGO_DB);

// Create a collection named 'services'
db.createCollection('services');
// Create a collection named 'teams'
db.createCollection('teams');

// Populate the 'services' collection
db.services.insertMany([
    {
        name: 'MongoDB',
        slug: 'mongo',
        description: 'MongoDB Database Service',
        image: "mongo",
        tag: "DB"
    },
    {
        name: 'Redis',
        slug: 'redis',
        description: 'Redis KV Store and Cache',
        image: "redis",
        tag: "DB"
    },
    {
        name: 'GitLab',
        slug: 'gitlab',
        description: 'GitLab Version Control System',
        image: "gitlab/gitlab-ce",
        tag: "VCS"
    },
    {
        name: 'WordPress',
        slug: 'wordpress',
        description: 'WordPress Content Management System',
        image: "wordpress",
        tag: "Web"
    },
    {
        name: 'Jenkins',
        slug: 'jenkins',
        description: 'Jenkins Continuous Integration and Delivery',
        image: "jenkins/jenkins",
        tag: "CI/CD"
    },
    {
        name: 'Postgres',
        slug: 'postgres',
        description: 'PostgreSQL Database Service',
        image: "postgres",
        tag: "DB"
    },
    {
        name: 'Elasticsearch',
        slug: 'elasticsearch',
        description: 'Elasticsearch Search Engine',
        image: "elasticsearch",
        tag: "Search"
    },
    {
        name: 'RabbitMQ',
        slug: 'rabbitmq',
        description: 'RabbitMQ Message Broker',
        image: "rabbitmq",
        tag: "Messaging"
    },
    {
        name: 'Kafka',
        slug: 'kafka',
        description: 'Apache Kafka Stream Processing',
        image: "kafka",
        tag: "Streaming"
    },
    {
        name: 'Prometheus',
        slug: 'prometheus',
        description: 'Prometheus Monitoring System',
        image: "prom/prometheus",
        tag: "Monitoring"
    },
    {
        name: 'Grafana',
        slug: 'grafana',
        description: 'Grafana Data Visualization',
        image: "grafana/grafana",
        tag: "Monitoring"
    },
    {
        name: 'Zulip',
        slug: 'zulip',
        description: 'Zulip Team Chat and Collaboration',
        image: "zulip/zulip",
        tag: "Messaging"
    },
    {
        name: 'HAProxy',
        slug: 'haproxy',
        description: 'HAProxy Load Balancer',
        image: "haproxy",
        tag: "Proxy"
    },
    {
        name: 'Consul',
        slug: 'consul',
        description: 'Consul Service Discovery and Configuration',
        image: "consul",
        tag: "Service Discovery"
    },
    {
        name: 'Vault',
        slug: 'vault',
        description: 'Vault Secrets Management',
        image: "vault",
        tag: "Security"
    },
    {
        name: 'Traefik',
        slug: 'traefik',
        description: 'Traefik Reverse Proxy and Load Balancer',
        image: "traefik",
        tag: "Proxy"
    },
    {
        name: 'Fluentd',
        slug: 'fluentd',
        description: 'Fluentd Log Collector',
        image: "fluent/fluentd",
        tag: "Logging"
    },
    {
        name: 'Logstash',
        slug: 'logstash',
        description: 'Logstash Data Processing Pipeline',
        image: "logstash",
        tag: "Logging"
    }
]);
