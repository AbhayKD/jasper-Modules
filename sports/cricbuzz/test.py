import xml.dom.minidom
import urllib2
import json

class Cricz(object):
    def __init__(self):
        self.__api_url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"

    def __get_basedata(self):
        try:
            makereq = urllib2.Request(self.__api_url, headers={'User-Agent': "Magic Browser"})
        except ConnectionError:
            raise ("Host Error please try again")
        content = urllib2.urlopen(makereq)
        doc = xml.dom.minidom.parse(content)
        node = doc.documentElement
        matches = node.getElementsByTagName("match")
        return matches

    def get_live_score(self):
        matches = self.__get_basedata()
        scores = self.__matchrepo(matches)
        return scores

    def __matchrepo(self, matches):
        score_data = {}
        btname = ' '
        bwname = ' '
        score_data["data"] = []
        for match in matches:
            ms = match.getAttribute
            if not ms('id'):
                match_id = 'None'
            match_id = ms('id')
            ''' get the current state details of the match '''
            for state in match.getElementsByTagName('state'):
                sm = state.getAttribute
                state = {"state":sm('mchState'), "status":sm('status'), "WhoToss":sm('TW'), \
                "session":sm('addnStatus'), "other":sm('splStatus')}
            ''' get the batting team details '''
            batting_team = {}
            batting_team['bt_score'] = []
            for bt in match.getElementsByTagName('btTm'):
                btname = bt.getAttribute('sName')
                '''Batting team inngs details '''
                for inngs in bt.getElementsByTagName('Inngs'):
                    btin = inngs.getAttribute
                    batting_team['bt_score'].append({"run":btin('r'), "desc":btin('desc'), "overs":btin('ovrs'), "wkts":btin('wkts'), \
                    "followon":btin('FollowOn'), "decl":btin('Decl')})
            ''' get the bowling team details '''
            bowling_team = {}
            bowling_team['bw_score'] = []
            for bw in match.getElementsByTagName('blgTm'):
                bwname = bw.getAttribute('sName')
                '''Bowling team inngs details '''
                for inngs in bw.getElementsByTagName('Inngs'):
                    bwin = inngs.getAttribute
                    bowling_team['bw_score'].append({"run":bwin('r'), "desc":bwin('desc'), "overs":bwin('ovrs'), "wkts":bwin('wkts'), \
                    "followon":bwin('FollowOn'), "decl":bwin('Decl')})
            score_data["data"].append({"match_"+match_id:[{"match_data":{"match_id":ms('id'), "type":ms('type'), "desc":ms('mchDesc'), \
            "match_no":ms('mnum'), "venue":ms('vcity'), "country":ms('vcountry'), "ground":ms('grnd'), \
            "inngscount":ms('inngCnt')}, "match_state": state, "batteam_score": batting_team, \
            "bowteam_score": bowling_team, "bt_name":btname, "bwl_team": bwname}]})

        return_data = score_data
        return return_data

    def match_data(self):
        live_score = self.get_live_score()
        match_data = {}
        match_data["result"] = []
        for data in live_score['data']:
            for key, value in data.iteritems():
                match_data["result"].append({"match_id":key, "match_no": data[key][0]['match_data']['match_no'],\
                "type": data[key][0]['match_data']['type'], "desc": data[key][0]['match_data']['desc']})
        return match_data

    def get_match(self, match_id):
        live_score = self.get_live_score()
        data = {}
        data['result'] = []
        for i in live_score['data']:
            if i.has_key(match_id):
                data['result'].append(i)
            else:
                pass
        return data
