#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ returns list of school having specific topic """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs
