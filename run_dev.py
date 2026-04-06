from app import create_app

application = create_app(is_test=True)

if __name__ == '__main__':
    application.run(
        host='0.0.0.0',
        port=5000,
        debug=True
        )