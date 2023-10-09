from decimal import *
from urllib.request import urlopen
from graph import stressTest, read_handler
import functionsPage
from functionsPage import addPlusTo, sortSOddsH, sortSOddsA, printResults, sortMLa, sortMLh, checkTeam
import json
from datetime import datetime, timedelta
from dynamo import *

#337912155331

def get_nfl_odds():

    keyFree = ""

    url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds?apiKey=" + keyFree + "&regions=us&markets=spreads,h2h&dateFormat=iso&oddsFormat=american"
    response = urlopen(url)
    data_json = json.loads(response.read())

    for i in data_json:

        gameID = i['id']
        ht = checkTeam(i['home_team'])
        at = checkTeam(i['away_team'])
        time_str = i["commence_time"]
        time_dt = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')  # Assuming the time is in this format
        current_time = datetime.utcnow()  # Assuming the time is in UTC

        # Check if the time is within the next 7 days
        if current_time <= time_dt <= (current_time + timedelta(days=7)):

            # if check == ht or check == at:

            array = []
            array2 = []
            hml = ""
            aml = ""
            for j in i['bookmakers']:

                bookKey = j['key']
                bookTitle = j['title']
                if (bookKey == 'draftkings' or bookKey == 'bovada' or bookKey == 'fanduel' or bookKey == 'betmgm' or bookKey == 'barstool' or bookKey == 'pointsbetus' or bookKey == 'wynnbet' or bookKey == "betrivers" or bookKey == 'williamhill_us'):

                    hspread = ""
                    hsprOdds = ""
                    aspread = ""
                    asprOdds = ""
                    for k in j['markets']:
                        # fix a few B keys

                        if bookKey == 'williamhill_us':
                            bookTitle = "Caesars"
                        if bookKey == 'pointsbetus':
                            bookTitle = "PointsBet"
                        if bookKey == 'barstool':
                            bookTitle = 'Barstool'

                        if k['key'] == "spreads":
                            if checkTeam(k['outcomes'][0]['name']) == ht:
                                hspread = k['outcomes'][0]['point']
                                hsprOdds = k['outcomes'][0]['price']
                                aspread = k['outcomes'][1]['point']
                                asprOdds = k['outcomes'][1]['price']
                            elif checkTeam(k['outcomes'][1]['name']) == ht:
                                hspread = k['outcomes'][1]['point']
                                hsprOdds = k['outcomes'][1]['price']
                                aspread = k['outcomes'][0]['point']
                                asprOdds = k['outcomes'][0]['price']
                            else:
                                print("spr what")
                        if k['key'] == "h2h":
                            if checkTeam(k['outcomes'][0]['name']) == ht:
                                hml = k['outcomes'][0]['price']
                                aml = k['outcomes'][1]['price']
                            elif checkTeam(k['outcomes'][1]['name']) == ht:
                                hml = k['outcomes'][1]['price']
                                aml = k['outcomes'][0]['price']
                            else:
                                print("ML what")
                    obj = functionsPage.Matchup(gameID, current_time, ht, at, bookTitle, hml, aml, hspread, hsprOdds, aspread,
                                                asprOdds)

                    array.append(obj)
                    array2.append(obj)

                    #sortMLh(array)
                    #sortSOddsH(array2)

            now = datetime.now()
            for el in array:
                print(el.gameID + " " + el.sportsbook + ": " + el.awayTeam + " (" + str(
                    el.aML) + ") vs. " + el.homeTeam + " (" + str(el.hML) + ")")
                #insert_into_dynamodb(el.gameID,now,el.sportsbook,el.homeTeam, el.awayTeam, el.hML, el.aML, Decimal(str(el.homeSpread)), Decimal(str(el.awaySpread)), el.homePrice, el.awayPrice)
                #ADD TO DYNAMO TABLE

    return ""

#stressTest()
read_handler()
