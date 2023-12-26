In order to make it run, you need to add etc folder in backend. In side this folder, a file "settings.json" should be present.
settings.json content: {
    "env": "dev",
    "database_uri": "mysql+pymysql://db_name:password@localhost/sis"
}
