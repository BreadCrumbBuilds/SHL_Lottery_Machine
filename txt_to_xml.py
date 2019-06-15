# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:29:16 2019

@author: brad.crump
"""
import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

file = open(".\\TeamStandings.txt", "r")
League = []


# Parse text file
for line in file:
    team, standing = line.split(":")
    standing = int(standing.strip())
    Team = team, standing
    League.append(Team)
    
print(League)



root = ET.Element('League')

for team in League:
    Team = ET.SubElement(root, "Team")
    
    XMLTeam = ET.SubElement(Team, "Owner", {"Name": team[0]})
    XMLStanding = ET.SubElement(Team, "Standing", {"Standing": str(team[1])})
    print(team[0])
    print(team[1])
    #teamName        = ET.SubElement(XMLTeam, team[0])
    #standing    = ET.SubElement(XMLStanding, str(team[1]))
    
    
Tree = ET.ElementTree(indent(root))

Tree.write('..\\Today\\Resource\\TeamStandings.xml', xml_declaration=True, encoding='utf-8')
    
