from django.db import models


# Create your models here.
class Resolution:
    def __init__(self):
        self.resolution = []


class Mistakes:
    def __init__(self):
        self.mistakes = dict()


class Link:
    def __init__(self):
        self.link = ''
