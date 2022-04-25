# from http import HTTPStatus

# from flask import current_app, jsonify, request

# from app.models.events_model import Events

# def create_events():
#     files = request.files

#     for obj in files:
#         if obj == "file":
#             event = Events(name = "EVENtooosssteste", event_date = "01/12/2023", link = files[obj])
#             current_app.db.session.add(event)
#             current_app.db.session.commit()
#         return jsonify(event), HTTPStatus.CREATED
#     return {},HTTPStatus.OK
