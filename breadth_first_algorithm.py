from collections import deque
from traceback import print_tb

def person_is_seller(name):
    return name[-1] == '_'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom_", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom_"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")