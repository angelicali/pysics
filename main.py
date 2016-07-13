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
import Problem as p

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
    def post(self):
    	id = self.request.get('q')
    	if id and id.isdigit():
    		id = int(id)
    		self.write("searching for %d...."%id)
    		self.write("Don't wait for it. It's not really searching.")


class CalculatorHandler(Handler):
	def get(self):
		self.render('calc.html')

		#cont = '''A horizontal turntable is made from a uniform solid disk and is initially rotating with&nbsp;angular velocity of 9.7 rad/s&nbsp;about a fixed vertical axis through its center. The turntable&nbsp;has a radius of 0.36 m and&nbsp;a moment of inertia of 0.17496 kg m<sup>2&nbsp;</sup>about the rotation axis.&nbsp;'''
		pid = 12345
		#vlst = ['omega','r','I','d','omegaf']
		#problem = p.Problem(content=cont,id=pid,vlst=vlst)
		#problem.put()

		prob1 = p.query_id(pid)
		self.write(prob1)


	def post(self):
		v_list = [12,34,56]
		pid = 12345
		ans = eval("qlist._%s(%s)"%(pid,v_list))
		self.render('calc.html',answer=ans)
		self.write("post")

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/calculator',CalculatorHandler)
], debug=True)
