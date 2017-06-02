import subprocess,json



def standings(league):
    command = "soccer --standings --league "+ league +" --json"
    data = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    stands = data.stdout.read()
    #data = subprocess.check_output(command, shell=True)
    return json.loads(stands)

def teamMatch(team):
    command = "soccer --team="+ team +" --time=10"
    data = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    match = data.stdout.read()
    array = match.strip()
    return array.splitlines()

def liveMatch():
    command = "soccer --live"
    data = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    match = data.stdout.read()
    if "NO LIVE" in match.upper():
        return ""
    else:
        array = match.strip()
        return array.splitlines()

teams = {"chelsea": "CFC","manchester united":"MUFC","Manchester city":"MCFC"}

abbre = {"champions league":"CL","premier league":"PL","league one":"EL1",\
         "french league":"FL","french league two":"FL2","bundesliga":"BL",\
         "bundesliga two":"BL2","bundesliga three":"BL3","seria a":"SA",\
         "netherlands league":"DED","eredivisie":"DED","premier liga":"PPL",\
         "la liga":"LLIGA","la liga second":"SD"}

if option == 0:
    name = raw_input("Enter the league: ")
    league = abbre.get(name)
    print league
    standings = standings(league)['standings']
    team = raw_input("Team name:")
    for obj in standings:
        if team.upper() in obj['teamName'].upper():
            print "Pos: ", obj['position'],"Team: ", obj['teamName'],\
                  "Points: ",obj['points']
elif option == 1:
    name = raw_input("Enter the league: ")
    league = abbre.get(name)
    print league
    standings = standings(league)['standings']
    for index, obj in enumerate(standings):
        print "Pos: ", obj['position'],"Team: ", obj['teamName'],\
              "Points: ",obj['points']
        if index == 5:
            break
elif option == 2:
    name = raw_input("Enter the Team: ")
    team = teams.get(name)
    print team
    matches = teamMatch(team)
    for i in matches:
        if i != '':
            print i[11:].split()
elif option == 3:
    matches = liveMatch()
    for i in matches:
        if i != '':
            print i[:-8].split()
        else:
            print "NO LIVE ACTION"
