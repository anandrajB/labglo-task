DATABASE_OPTIONS = {
    "OPTIONS": {
        "max_connections": 2000,
        "OPTIONS": {
            "sslmode": "require",
            "sslcert": "/path/to/client-certificate.crt",
            "sslkey": "/path/to/client-key.key",
            "sslrootcert": "/path/to/ca-certificate.crt",
        },
        "POOL": {
            "max_overflow": 10,
            "pool_size": 5,
            "timeout": 30,
        },
    }
}
