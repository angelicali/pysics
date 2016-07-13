from google.appengine.ext import ndb

class Problem(ndb.Model):
	content = ndb.TextProperty(required=True)
	id = ndb.IntegerProperty(required=True)
	vlst = ndb.JsonProperty()

def query_id(id):
	qry = Problem.query().filter(Problem.id == id)
	return qry.fetch()
