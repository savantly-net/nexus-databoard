import os

PROJECT_DIRECTORY = f"{os.path.dirname(os.path.realpath(__file__))}/.."

VERSION = file = open(f"{PROJECT_DIRECTORY}/VERSION", "r").read()

# Database
DB_DIALECT = "postgresql+psycopg2"
DB_HOST = "localhost"
DB_PORT = 5432
DB_DATABASE = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

# Site
SITE_URL = "http://localhost:8501"
SITE_NAME = "Savantly Analytics"
SITE_DESCRIPTION = """
# Savantly Analytics
This provides a solution for customized analytics applications.  
Contact your solutions engineer for more information.  
[support@savantly.net](mailto://support@savantly.net)  
"""

# Authz
EXTERNAL_AUTH_ENABLED = False


# DEVELOPMENT ONLY
DEV_MODE = False
DEV_ROLE = "ADMIN"

HOME_PAGE_HEADER = "# Savantly Projects"