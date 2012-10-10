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

from django.shortcuts import render_to_response
from django.http import Http404
from posts import Posts

p = Posts()

def home(request):
    return render_to_response('posts.html', {
            "posts": p.home_posts(),
            "next_url": "/index_1/"
            })

def posts(resquest, post_id):

    tmp = int(post_id)

    #check if this page exists
    post_list = p.id_posts(tmp)
    if len(post_list) == 0:
        raise Http404


    #check if there is a next page
    is_next_page = True
    next_list = p.id_posts(tmp + 1)
    if len(next_list) == 0:
        is_next_page = False

    return render_to_response('posts.html', {
            "posts": post_list,
            "next_url": "/index_" + str(tmp + 1) + "/",
            "is_next_page": is_next_page
            })