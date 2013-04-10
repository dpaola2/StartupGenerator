#! /usr/bin/env python

import requests, json, time

FILENAME = "ideas.json"

def open_ideas():
    try:
        return json.loads(open(FILENAME, "r").read())
    except:
        return {"this": {}, "that": {}}

def write_ideas(ideas):
    print "Writing %s..." % FILENAME
    return open(FILENAME, "w").write(json.dumps(ideas, indent = 2))

def main():
    ideas = open_ideas()
    count = 0
    while count < 25:
        print "querying...",
        try:
            idea = requests.get("http://itsthisforthat.com/api.php?json").json()
            print "response: %s" % idea,
            this = idea["this"]
            that = idea["that"]
            ideas["this"][this] = 1
            ideas["that"][that] = 1
        except Exception, e:
            print e
        finally:
            write_ideas(ideas)
        count += 1
        print "sleeping for 1 second."
        time.sleep(1)
    print "Quitting with %s keys and %s values!!" % (len(ideas["this"].keys()), len(ideas["that"].keys()))

if __name__ == '__main__':
    main()
