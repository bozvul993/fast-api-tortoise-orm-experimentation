data_base_config = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'local_dev',
                'password': 'local_dev',
                'database': 'local_db',
            }
        }
    },
    'apps': {
        'models': {
            'models': ['_models_'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}