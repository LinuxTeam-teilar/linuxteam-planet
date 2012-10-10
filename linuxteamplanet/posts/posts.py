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
from models import PostsModel
from dateutil.parser import parse

class Posts(object):
    def __init__(self):
        self._feeds = Feeds(path.join(path.dirname(path.realpath(__file__)) + '/../../configs', 'config.json'))
        self._markdown = MD("/opt/github/linuxteam-planet-sources/")
        self._populateDb()

    def home_posts(self):
        return PostsModel.object.order_by()[:5]

    def id_posts(self, id):
        start = id * 5
        end = start + 5
        return PostsModel.object.order_by()[start:end]

    def _populateDb(self):
        l = self._markdown.elements
        l += self._feeds.elements

        for it in l:
            p = None
            _date = parse(it["date"].split('+')[0])
            try:
                p = PostsModel(author = it["author"], title = it["title"], link = it["link"], content = it["content"], date = _date, isInternalPost = False)
            except KeyError:
                p = PostsModel(author = it["author"], title = 'aaaa', link = it["link"], content = it["content"], date = _date, isInternalPost = False)
            p.save()
