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
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#class MainHandler(webapp2.RequestHandler):
#	def get (self):
#        path = self.response.path
#		template = JINJA_ENVIRONMENT.get_template('templates' + path)
#		self.response.write(template.render())

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'HOME'}))
    	#if you need to render two elements, replace above line with this one
    	 #self.response.write(template.render({'title': 'HOME', 'name':'Colleen'}))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render())

    def post(self):
        username = "Colleen"
        password = "pass"

        if ((self.request.get('user') == username) and (self.request.get('pass') == password)):
            template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
            self.response.write(template.render())
        else:
            #self.response.write("Bad credentials. Try again.</br></br>")
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'prompt':'Bad credentials. Try again.'}))
            logging.info("Bad credentials. Try again.")
            logging.info("Username: " + self.request.get('user'))
            logging.info("Password: " + self.request.get('pass'))

class FamilyHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/family.html')
    	self.response.write(template.render())


class FoodHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/food.html')
     	self.response.write(template.render())


app = webapp2.WSGIApplication([
#	('/', MainHandler)
    ('/', IndexHandler),
    ('/login', LoginHandler),
    ('/index', IndexHandler),
    ('/family', FamilyHandler),
    ('/food', FoodHandler)
], debug=True)
