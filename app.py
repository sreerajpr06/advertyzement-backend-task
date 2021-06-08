from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema, BankBranches

app = Flask(__name__)
app.debug = True

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