import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponde
from src.models.repository.events_repository import EventsRepository

class AttendeesHandler:
  def __init__(self) -> None:
    self.__attendees_repository = AttendeesRepository()
    self.__event_repository = EventsRepository()

  def registry(self, http_request: HttpRequest) -> HttpResponde:
      body = http_request.body
      event_id = http_request.param["event_id"]

      event_attendees_count = self.__event_repository.count_event_attendees(event_id)
      if (
        event_attendees_count["attendeesAmount"] 
        and event_attendees_count["maximumAttendees"] < event_attendees_count["attendeesAmount"]
      ): raise Exception("Evento Lotado")

      body["uuid"] = str(uuid.uuid4())
      body["event_id"] = event_id
      self.__attendees_repository.insert_attendee(body)

      return HttpResponde(body=None, status_code=201)
  
  def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponde:
      attendee_id = http_request.param["attendee_id"]
      badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
      if not badge: raise Exception("Participante nao encontrado")

      return HttpResponde (
         body= {
            "badge": {
               "name": badge.name,
               "email": badge.email,
               "eventTitle": badge.title,
            }
         },
         status_code= 200
      )