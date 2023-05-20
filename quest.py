RouteNode = {
    "routeTree": {
        "route": "/",
        "title": "Карта",
        "children": [
            {
                "route": "stars",
                "title": "Звезды",
                "children": [
                    {
                        "route": "starId"
                    }
                ]
            },
            {
                "route": "constellations",
                "title": "Созвездия"
            },
            {
                "route": "constellation",
                "redirectTo": "constellations",
                "children": [
                    {
                        "route": "constellationId",
                        "children": [
                            {
                                "route": "stars",
                                "title": "Звезды",
                                "children": [
                                    {
                                        "route": "starId"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
#  "data": {
#    "constellation": {
#      "1": "Лира",
#      "2": "Орион"
#    },
#    "star": {
#      "1": "Вега",
#      "2": "Бетельгейзе"
#    }
#  },
#  "urls": ["/stars/1", "/constellation/2/stars/2"]

path = []
title = []
root = RouteNode['routeTree']
num = 0

print(root)


def func(object):
    def children_loop(static_object, i):
        i = i - 1
        path.append('/' + static_object['route'])
        if 'title' in static_object.keys():
            title.append(static_object['title'])
        else:
            title.append('None')
        if 'children' in static_object.keys():
            if len(static_object['children']) > 0:
                sublen = len(static_object['children'])
                children_loop(static_object['children'][0], sublen)
        else:
            return i
    path.append(object['route'])
    if 'title' in object.keys():
        title.append(object['title'])
    else:
        title.append('')
    if 'children' in object.keys():
        num = len(object['children'])
        for i in range(num):
            children_loop(object['children'][i], i)
    else:
        print('num')


func(root)
print(path)
print(title)
