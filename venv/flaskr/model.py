from monoengine import *
class Game(document):
	name = StringField(max_length = 100, required = True)
	appid = ObjectIdField(required = True, primary_key = True, verbose_name = """The app Id of the game""")
	logo = StringField(max_length = 100)
	icon = StringField(max_length = 100)

class User(document):
	name = StringField(max_length = 100, required = True)
	userid = ObjectIdField(max_length = 100 , required = True , primary_key = True)
	played = ListField((IntField,ReferenceField(Game)))

class Team(Document):
	users = ListField(ReferenceField(User))

class Tournament(EmbeddedDocumentField):


class EventId(Document):
	games = ListField((ReferenceField(Game),DateTimeField(required = True),DateTimeField,EmbeddedDocumentField(Tournament)))
	teamCompositions = ListField(ReferenceField(Team))
	teamMatchups = ListField((ReferenceField(Team),ReferenceField(Team)))
