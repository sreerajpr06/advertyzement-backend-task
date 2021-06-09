from flask import Flask
from flask_graphql import GraphQLView

from schema import schema

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Goto /gql"

app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'gql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run()