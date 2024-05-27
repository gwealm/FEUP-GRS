// Connect to the admin database
db = db.getSiblingDB('admin');

// Authenticate using environment variables
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);

// Switch to the default database
db = db.getSiblingDB(process.env.MONGO_DB);

// Create a collection named 'services'
db.createCollection('services');

// Populate the 'services' collection
db.services.insertMany([
    {
        name: 'MongoDB',
        description: 'MongoDB Database Service',
        image: "redis",
        tag: "DB"
    },
    {
        name: 'Redis',
        description: 'Redis KV Store and Cache',
        image: "mongo",
        tag: "DB"
    },
    {
        name: 'GitLab',
        description: 'GitLab Version Control System',
        image: "gitlab/gitlab-ce",
        tag: "VCS"
    },
    {
        name: 'Squid Proxy',
        description: 'Squid Forward Proxy',
        image: "ubuntu/squid:latest",
        tag: "Proxy"
    },
]);