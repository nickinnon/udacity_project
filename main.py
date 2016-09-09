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

form='''
<h1>Test Encryption</h1>
<form method='post'>
    <textarea type="text" name="text"></textarea>
    <br>
    <br>
    <input type="submit" value="Submit">
    <div name="">%(output)s<div>
</form>
'''

class MainHandler(webapp2.RequestHandler):
    def write_form(self, output=""):
        self.response.out.write(form % {"output": output})

    def get(self):
        self.write_form()

    def post(self):
        text_input = self.request.get('text')

        output = self.rot13(text_input)
        self.write_form(output)
            #this does not sanitize HTML
            #possible defects:
            #   user may be able to manipulate HTML styles in browser


    def rot13(self, s):
        result = ""
        for v in s:
            c = ord(v)
            if c >= ord('a') and c<= ord('z'):
                if c > ord('m'):
                    c -= 13
                else:
                    c += 13
            elif c >= ord('A') and c <= ord('Z'):
                if c > ord('M'):
                    c -= 13
                else:
                    c += 13
            result += chr(c)
        return result


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
