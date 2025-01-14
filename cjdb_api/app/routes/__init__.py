from flask import Blueprint
from flask_restful import Api
import  cjdb_api.app.resources.querying as query


api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

#routes
api.add_resource(query.UpdateAttrib, "/update/<string:object_id>/<string:attrib>/<string:new_value>")
api.add_resource(query.show, "/show/<int:lim>")
api.add_resource(query.DelObject, "/delObject/<string:object_id>")
api.add_resource(query.QueryByPoint, "/point/<string:coor>")
api.add_resource(query.QueryByBbox, "/bbox/<string:coor>")
api.add_resource(query.CalculateFootprint, "/area/<string:object_id>")
api.add_resource(query.AddAttribute, "/add/<string:object_id>/<string:attrib>/<string:new_value>")
api.add_resource(query.DelAttrib, "/del/<string:object_id>/<string:attrib>")
api.add_resource(query.CQL_query, "/cql")
api.add_resource(query.FilterAttributes, "/filter/<string:attrib>/<string:operator>/<string:value>")
api.add_resource(query.GetChildren, "/children/<string:object_id>")
api.add_resource(query.GetParent, "/parent/<string:object_id>")
api.add_resource(query.QueryByAttribute, "/select/<string:attrib>/<string:value>")
api.add_resource(query.GetInfo, "/info/<string:attrib>/<string:object_id>")

#route that can load query parameters
api.add_resource(query.Item,"/items")
