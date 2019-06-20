#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:08:31 2019

@author: BradleyCrump
"""

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Congratulations, it's a web app!")

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)