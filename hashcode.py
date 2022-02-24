#!/usr/bin/env python3
import sys
import os
from math import *

contributors = 0
projectNumber = 0

class Person:
    def __init__(self, name, numberSkills):
        self.name = name
        self.number = numberSkills
        self.skills = []
    def addSkill(self, skill):
        self.skills.append(skill)
    def getName(self):
        return self.name
    def hasSkill(self, skill):
        tmp = skill.split(" ")
        for i in range(len(self.skills)):
            tmp2 = self.skills[i].split(" ")
            if tmp2[0] == tmp[0]:
                if int(tmp2[1]) >= int(tmp[1]) - 1:
                    return True
        return False


class Project:
    def __init__(self, name, duration, score, best, numberSkills):
        self.name = name
        self.duration = duration
        self.score = score
        self.best = best
        self.numberSkills = numberSkills
        self.skills = []
    def addSkill(self, skill):
        self.skills.append(skill)
    def getSkills(self):
        return self.skills
    def getName(self):
        return self.name
    def getNumber(self):
        return self.numberSkills

def main():
    try: file = open(sys.argv[1], "r")
    except: sys.exit(84)
    lines = file.readlines()
    s = lines[0].split(" ")
    personList = []
    projectList = []
    contributors = s[0]
    projectNumber = s[1]

    i = 0
    n = 0
    o = 1
    while i < int(contributors):
        tmp = lines[o].split(" ")
        t = int(tmp[1])
        new = Person(tmp[0], tmp[1])
        personList.append(new)
        while n < t:
            n += 1
            u = lines[o+n].split(" ")
            new.addSkill(lines[o+n])
        i += 1
        o += n + 1
        n = 0
        tmp.clear()

    i  = 0
    n = 0
    while i < int(projectNumber):
        tmp = lines[o].split(" ")
        t = int(tmp[4])
        new = Project(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4])
        projectList.append(new)
        while n < t:
            n += 1
            u = lines[o+n].split(" ")
            new.addSkill(u)
        i += 1
        o += n + 1
        n = 0
        tmp.clear

    f = open("rendu.txt", "a")
    f.write(projectNumber)
    z = 0
    for i in projectList:
        f.write(i.getName())
        f.write('\n')
        for t in i.getSkills():
            for p in personList:
                tmp = t[0] + " " + t[1]
                if (p.hasSkill(tmp)):
                    f.write(p.getName())
                    if z < (int(i.getNumber()) - 1):
                        f.write(" ")
                    break
            z += 1
        z = 0
        f.write('\n')



if __name__ == '__main__':

    main()
