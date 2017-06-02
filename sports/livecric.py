from espncricinfo.summary import Summary
import json

def getOvers(s):
    scoreN = s.replace("&amp;","")
    score = scoreN.split('(')[0]
    overs = scoreN.partition('(')[-1].rpartition('&')[0]
    return score,overs

s = Summary().all_matches


for obj in s:
    print obj['team2_name'], "VS", obj['team1_name']
    if 'result' in obj:
        print obj['result']
    score, overs = getOvers(obj['team2_score'])
    print "Team2", score, " ", overs
    score, overs = getOvers(obj['team1_score'])
    print "Team1", score, " ", overs
    #print obj['team2_score']
    #print obj['team1_score']
    if 'live_state' in obj:
        print obj['live_state']
    print '-------------------------'
