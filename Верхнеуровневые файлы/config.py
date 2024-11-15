import os

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_2420_exam:11111111@std-mysql.ist.mospolytech.ru/std_2420_exam'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'media', 'images')
