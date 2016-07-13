#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import problem_list as plist

FOLDERNAME = "templates" 	# only for self.render(template)   e.g. html files


template_dir = os.path.join(os.path.dirname(__file__), FOLDERNAME)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

	def set_ck(self,cookie):
		self.response.headers.add_header('Set-Cookie',cookie)

	def get_ck(self,cookie):
		return self.request.cookies.get(cookie)

class MainHandler(Handler):
    def get(self):
        self.render('home.html')


class CalculatorHandler(Handler):
	def get(self):
		self.render('calc.html')
	def post(self):
		v_list = [12,34,56]
		qid = 12345
		ans = eval("qlist._%s(%s)"%(qid,v_list))
		self.render('calc.html',answer=ans)
		self.write("post")

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/calculator',CalculatorHandler)
], debug=True)
