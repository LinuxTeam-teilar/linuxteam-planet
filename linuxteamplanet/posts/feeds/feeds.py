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
import json
import logging
import feedparser

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Feeds(object):
    def __init__(self, feedsConfigFile):
        with open(feedsConfigFile) as f:
            self.json = json.load(f)

    @property
    def elements(self):
        list = []
        blogs = self.json["Configs"]["feeds"]
        for blog in blogs:
            logger.debug(blog["source"])
            logger.debug(blog["author"] + '\n' + '\n')
            parser = feedparser.parse(blog["source"])
            for entry in parser.entries:

                ok = True

                date = None

                try:
                    date = entry.published
                except AttributeError:
                    try:
                        date = entry.updated
                    except AttributeError:
                        ok = False

                if ok:
                    data = {
                        "author": blog["author"],
                        "title": entry.title,
                        "link": entry.link,
                        "content": entry.content[0]["value"],
                        "date": date,
                        "isInternalPost": False
                    }
                    list.append(data)
        return list
