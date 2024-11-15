import os

SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_2420_exam:11111111@std-mysql.ist.mospolytech.ru/std_2420_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')
