from src.models.settings.connection import db_connection_handler
from src.models.repository.events_repository import EventsRepository
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
  event = {
    "uuid":"meu-uuid-id-teste",
    "title":"meu-title-here",
    "slug":"meu-slug-aqui",
    "maximum_attendees":20,
  }

  events_repository = EventsRepository()
  response = events_repository.insert_event(event)
  print(response)


@pytest.mark.skip(reason="Nao necessita")
def test_get_event_by_id():
  event_id = "meu-uuid-id-teste"
  events_repository = EventsRepository()
  response = events_repository.get_event_by_id(event_id)
  print(response)