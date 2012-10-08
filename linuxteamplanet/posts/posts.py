#  Copyright 2012 by Giorgos Tsiapaliokas <terietor@gmail.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; see the file COPYING.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.

from os import path
from feeds.feeds import Feeds
from md.md import MD

class Posts(object):
    def __init__(self):
        #self._feeds = Feeds(path.join(path.dirname(path.realpath(__file__)) + '/../../configs', 'config.json'))
        self._markdown = MD("/opt/github/linuxteam-planet-sources/")
        self._url = ""

    def _posts(self):
        l = self._markdown.elements
        #l += self._feeds.elements

        #sort the list according to the date
        sorted(l, key = lambda date: date)
        return l

    def home_posts(self):
        pass

    def postsId(self, id):
        get_list = lambda x,y:[x[i:i+y] for i in range(0,len(x),y)]
        a = get_list(self._posts(), id)
        #print a
        return a
        pass

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url