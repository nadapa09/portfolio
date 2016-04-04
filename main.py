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

import os
import urllib
import webapp2
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        path = self.request.path
        if path == '/index':
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'title': 'Welcome'}))
        elif path == '/gallery':
            template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
            self.response.write(template.render({'title': 'Gallery'}))
        elif path == '/resume':
            template = JINJA_ENVIRONMENT.get_template('templates/resume.html')
            self.response.write(template.render({'title': 'Resume'}))
        elif path == '/activities':
            template = JINJA_ENVIRONMENT.get_template('templates/activities.html')
            self.response.write(template.render({'title': 'Activities'}))
        elif path == '/contact':
            template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
            self.response.write(template.render({'title': 'Contact Me'}))
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'title': 'Welcome'}))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render())

    def post(self):
        username = "Nithin"
        password = "Adapa"

        if ((self.request.get('user') == username) and (self.request.get('pass') == password)):
            template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
            self.response.write(template.render())
        else:
            #self.response.write("Bad credentials. Try again.</br></br>")
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'prompt':'Bad Credentials. Try Again.'}))
            logging.info("Bad credentials. Try again.")
            logging.info("Username: " + self.request.get('user'))
            logging.info("Password: " + self.request.get('pass'))

#class LoginHandler(webapp2.RequestHandler):
#    def get(self):
#        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
#        self.response.write(template.render())
#
#    def post(self):
#        validation = ["Nithin":"Adapa", "Colleen":"Professor", "Master":"Key"]
#        for x, y in validation.iteritems():
#            if ((x == self.request.get('user')) && (y == self.request.get('pass')) :    
#                template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
#                self.response.write(template.render())
#                temp = false;
#                break;
#
#        if (temp):
#            #self.response.write("Bad credentials. Try again.</br></br>")
#            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
#            self.response.write(template.render({'prompt':'Bad Credentials. Try Again.'}))
#            logging.info("Bad credentials. Try again.")
#            logging.info("Username: " + self.request.get('user'))
#            logging.info("Password: " + self.request.get('pass'))
#


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index', MainHandler),
    ('/gallery', MainHandler),
    ('/resume', MainHandler),
    ('/activities', MainHandler),
    ('/contact', MainHandler),
    ('/login', LoginHandler)
], debug=True)
