#! /usr/bin/env python

import requests, json, time

FILENAME = "ideas.json"

def open_ideas():
    try:
        return json.loads(open(FILENAME, "r").read())
    except:
        return {}

def write_ideas(ideas):
    print "Writing %s..." % FILENAME
    return open(FILENAME, "w").write(json.dumps(ideas))

def main():
    ideas = open_ideas()
    count = 0
    while count < 50:
        print "querying...",
        idea = requests.get("http://itsthisforthat.com/api.php?json").json()
        print "response: %s" % idea,
        ideas[idea["this"]] = idea["that"]
        count += 1
        print "sleeping for 1 second."
        time.sleep(1)
    write_ideas(ideas)
    print "Quitting with %s ideas!" % len(ideas.keys())
    

if __name__ == '__main__':
    main()
