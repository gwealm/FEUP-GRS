// Connect to the admin database
db = db.getSiblingDB('admin');

// Authenticate using environment variables
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);

// Switch to the default database
db = db.getSiblingDB(process.env.MONGO_DB);

// Create a collection named 'services'
db.createCollection('services');