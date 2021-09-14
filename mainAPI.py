

from ariadne.executable_schema import make_executable_schema
from ariadne.utils import gql
from ariadne import QueryType
from ariadne.asgi import GraphQL

from fastapi import FastAPI


type_defs = gql("""
    type Query{
        hello: String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(*_):
    return "Hell0 ..."

schema = make_executable_schema(type_defs, query)

app = FastAPI()
app.add_route("/", GraphQL(schema))