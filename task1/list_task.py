#----one-----#
justice_league =['Superman', 'Batman', 'Wonder Women', 'Flash', 'Aquaman','Green Lantern']
print("Justice League Members:", justice_league)
print("Number of members in Justice League:", len(justice_league))
#----two-----
justice_league.append('batgirl')
justice_league.append('NightWing')
print("Updated Justice League Members:", justice_league)
#----three-----#
justice_league.remove('Wonder Women')
justice_league.insert(0,'Wonder Women')
print("After making WW the leader Justice League Members:", justice_league)
#----four-----#
justice_league.remove('Green Lantern')
flashy=justice_league.index('Flash')
justice_league.insert(flashy,'Green Lantern')
print("seperating aquaman and flash: ",justice_league)
#----five-----#
justice_league=["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League Members:", justice_league)
justice_league.sort()
print("Sorted New Justice League Members:", justice_league)
print("new leader(0th index):", justice_league[0])