# user/__init__.py
import pymysql
pymysql.install_as_MySQLdb()

default_app_config = 'operation.apps.OperationConfig'