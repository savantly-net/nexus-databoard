from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="ANALYTICS",
    settings_files=["src/default-settings.py", "settings.py", "local_settings.py", ".secrets.py"],
)

project_dir = settings.PROJECT_DIRECTORY

version = settings.VERSION

db_dialect = settings.DB_DIALECT
db_user = settings.DB_USER
db_password = settings.DB_PASSWORD
db_host = settings.DB_HOST
db_port = settings.DB_PORT
db_database = settings.DB_DATABASE

site_url = settings.SITE_URL
site_name = settings.SITE_NAME
site_description = settings.SITE_DESCRIPTION

# Authz
external_auth_enabled = settings.EXTERNAL_AUTH_ENABLED


# DEVELOPMENT ONLY
dev_mode = settings.DEV_MODE
dev_role = settings.DEV_ROLE
