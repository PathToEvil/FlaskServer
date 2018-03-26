from flask_restful import Resource, fields, marshal_with
from FlaskServer.controllers.flask_restful import fields as jf_fields
from FlaskServer.controllers.flask_restful import parsers
from FlaskServer.models import db, User, Post, Tag
from flask import abort


nexted_tag_fields = {
    'id': fields.String(),
    'name': fields.String()
}

post_fields = {
    'author': fields.String(attribute=lambda x: x.user.username),
    'title': fields.String(),
    'text':  jf_fields.HTMLField(),
    'tags': fields.List(fields.Nested(nexted_tag_fields)),
    'publish_date': fields.DateTime(dt_format='iso8601')
}

class PostApi(Resource):

    @marshal_with(post_fields)
    def get(self, post_id = None):

        if post_id:
            post = Post.query.filter_by(id=post_id).first()
            if not post:
                abort(404)
            return post
        else:
            args = parsers.post_get_parser.parse_args()
            page = args['page'] or 1

            if args['user']:
                user = User.query.filter_by(username=args['user']).first()
                if not user:
                    abort(404)
                posts = user.posts.order_by(
                    Post.publish_date.desc()
                ).paginate(page, 30)
            else:
                posts = Post.query.order_by(
                    Post.publish_date.desc()
                ).paginate(page, 30)
            return posts.items


