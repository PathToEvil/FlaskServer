from flask_restful import reqparse

post_get_parser = reqparse.RequestParser()

post_get_parser.add_argument(
    'page',
    type=int,
    location=['json', 'args', 'headers'],
    required=False
)

post_get_parser.add_argument(
    'user',
    type=str,
    location=['json', 'args', 'headers']
)
