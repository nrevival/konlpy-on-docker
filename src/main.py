import connexion

# https://github.com/hjacobs/connexion-example 를 참조하세요

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=8090, specification_dir='swagger/')
    app.add_api('test.yaml', arguments={'title': 'Hello World Example'})
    app.run()