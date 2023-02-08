# project configuration file
import pathlib


SECRET_KEY = 'kungurcoders'

#SQLALCHEMY
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MAIL
MAIL_SERVER		= 'smtp.googlemail.com'
MAIL_PORT		= 587
MAIL_USE_TLS	= True
MAIL_USERNAME	= 'plutonplutonskij@gmail.com'
MAIL_PASSWORD	= 'Plutonec123'

# STATIC & MEDIA
MEDIA_ROOT		= pathlib.Path(__file__).resolve().parent.parent / 'static' / 'media' / 'profile_pics'
MEDIA_URL		= 'media/profile_pics' 
