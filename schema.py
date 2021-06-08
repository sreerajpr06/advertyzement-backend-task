import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import BankBranches as BankBranchesModel


class BankBranches(SQLAlchemyObjectType):
    class Meta:
        model = BankBranchesModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_branches = SQLAlchemyConnectionField(BankBranches.connection)


schema = graphene.Schema(query=Query)