# run server localy

# import variable app from root/app.py file
from app import app


if __name__ == '__main__':
    app.debug = True
    app.run()
