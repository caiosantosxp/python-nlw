import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponde


class EventHandler:
  def __init__(self) -> None:
    self.__event_repository = EventsRepository()

  def register(self, http_request: HttpRequest) -> HttpResponde:
      body = http_request.body
      body["uuid"] = str(uuid.uuid4())
      self.__event_repository.insert_event(body)

      return HttpResponde(
         body={ "eventId": body["uuid"]},
         status_code=200
      )

  def find_by_id(self, http_request: HttpRequest) -> HttpResponde:
      event_id = http_request.param["event_id"]
      event = self.__event_repository.get_event_by_id(event_id)
      if not event: raise Exception("Evento nao encontrado")

      event_attendees_count = self.__event_repository.count_event_attendees(event_id)

      return HttpResponde(
         body={
            "event": {
               "id": event.id,
               "title": event.title,
               "details": event.details,
               "slug": event.slug,
               "maximumAttendees": event.maximum_attendees,
               "attendeesAmount": event_attendees_count["attendeesAmount"]
            }
         },
         status_code=200
      )