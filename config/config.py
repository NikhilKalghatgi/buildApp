import json

config_file_path = "config.json"
with open(config_file_path) as config_file:
    config = json.load(config_file)

class Config:
    JWT_SECRET_KEY = config.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = 18000
    SQLALCHEMY_DATABASE_URI = config.get("DATABASE_URI")
    DB_URI = config.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'tm_scenario_catalogue': config.get('SCENARIO_CATALOGUE_DB_URI'),
        'tm_close_loop': config.get('CLOSED_LOOP_DB_URI'),
        'tm_automate_kpi_tja_v2': config.get('TJA_V2_AUTOMATE_KPI_DB_URI'),
        'tm_scene_gen': config.get('SCENE_GEN_DB_URI'),
        'tm_automate_kpi_tja_v1': config.get('TJA_V1_AUTOMATE_KPI_DB_URI')
    }
    MONGO_DB_CLOSE_LOOP_ALIAS = config.get('CLOSE_LOOP_MONGO_DB')
    MONGODB_DB = config.get("LKA_DATABASE")
    MONGODB_SETTINGS = [
        {
            'ALIAS': MONGO_DB_CLOSE_LOOP_ALIAS,
            'DB': MONGO_DB_CLOSE_LOOP_ALIAS,
            'HOST': 'localhost',
            'PORT': 27017
        },

       {
            'ALIAS': MONGODB_DB,
	        'DB': MONGODB_DB,
	        'HOST': 'localhost',
	         'PORT': 27017
        }
    ]
    SCENARIO_CATALOGUE_DB_URI = config.get('SCENARIO_CATALOGUE_DB_URI')
    SCENE_GEN_DB_URI = config.get('SCENE_GEN_DB_URI')
    SCENARIO_CATALOGUE_MONGO_DB_NAME = config.get('SCENARIO_CATALOGUE_MONGO_DB_NAME')
    DATA_PER_PAGE = 25
    DB_SERVER = config.get("DB_SERVER")
    DB_NAME = config.get("DB_NAME")
    DB_NAME_TJA = config.get("DB_NAME_TJA")
    DB_AUTOMATE_KPI_TJA_V2 = config.get("DB_AUTOMATE_KPI_TJA_V2")
    TJA_V1_CSV_FILES_PATH = config.get("TJA_V1_CSV_FILES_PATH")
    TJA_V2_CSV_FILES_PATH = config.get("TJA_V2_CSV_FILES_PATH")
    TJA_V2_VIDEO_FILES_PATH = config.get("TJA_V2_VIDEO_FILES_PATH")
    DB_USER = config.get("DB_USER")
    DB_PWD = config.get("DB_PWD")
    APPLICATION_DEFAULT_LANDING_PAGE = config.get("APPLICATION_DEFAULT_LANDING_PAGE")
    MONGODB_HOST = config.get("MONGO_SERVER")
    MONGODB_PORT = config.get("MONGO_PORT")

    MONGO_URI = "mongodb://{}:{}/".format(config.get("MONGO_SERVER"), config.get("MONGO_PORT"))

    CUSTOMIZED_SCENARIO_CATALOGUE = True

    DIRECTORY = config.get("DIRECTORY")
    BENCH_PING_TIMEOUT = config.get("BENCH_PING_TIMEOUT")
    BENCH_DATA = config.get("BENCH_DATA")
    VERSION = config.get("VERSION")
    DATASET = config.get("DATASET")
    MFDB_PATH = config.get("K_DATA_ANALYZER").get("MFDB_PATH")
    CSV_PATH = config.get("K_DATA_ANALYZER").get("CSV_PATH")

    DATA_PATH = config.get("SCENE_EXTRACT").get("DATA_PATH")

    ARANGO_COLLECTION_JSON_PATH = config.get("SCENARIO_EDITOR").get("ARANGO_COLLECTION_JSON_PATH")
    ARANGO_EDGE_JSON_PATH = config.get("SCENARIO_EDITOR").get("ARANGO_EDGE_JSON_PATH")
    ARANGO_FILTER_COLLECTION_JSON_PATH = config.get("SCENARIO_EDITOR").get("ARANGO_FILTER_COLLECTION_JSON_PATH")
    ARANGO_FILTER_EDGE_JSON_PATH = config.get("SCENARIO_EDITOR").get("ARANGO_FILTER_EDGE_JSON_PATH")

    CARLA_DATASET = config.get("CARLA_DATASET")
    CARLA_CSV_SETS = config.get("CARLA_CSV_SETS")
    MONGOALCHEMY_DATABASE =  config.get("MONGOALCHEMY_DATABASE")
    MONGOALCHEMY_SERVER = config.get("MONGOALCHEMY_SERVER")
    MONGOALCHEMY_PORT = config.get("MONGOALCHEMY_PORT")
    SCHEME_BENCH = config.get("SCHEME")
    MODE = config.get("MODE")

    SERVICES = [
        {"path": ".server.routes", "blueprint": "server"}
    ]
    URL =  config.get('SCHEME')+'://' + BENCH_DATA['benchData'][0]['address'] + ':' + config.get("PORT")
    BENCH_URL = config.get('SCHEME') + '://' + BENCH_DATA['benchData'][0]['address'] + ':' + BENCH_DATA['benchData'][0]['http_port']
    CELERY_CONFIG = config.get('CELERY_CONFIG')
