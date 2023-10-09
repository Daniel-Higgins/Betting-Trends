from dynamo import *
import matplotlib.pyplot as plt
import io
import matplotlib.dates as mdates


def stressTest():
    now = datetime.now()
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-26 09:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-125", "150", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-26 09:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-220", "232", "-10.5", "10.5", "-110", "-110")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-26 21:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-125", "150", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-26 21:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-220", "232", "-10.5", "10.5", "-110", "-110")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-27 09:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-120", "140", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-27 09:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-220", "250", "-8.5", "8.5", "-115", "-110")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-27 21:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-120", "145", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-27 21:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-220", "255", "-8.5", "8.5", "-115", "-110")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-28 09:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-120", "110", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-28 09:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-227", "250", "-8.5", "8.5", "-110", "-110")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-28 21:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-125", "115", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-28 21:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-220", "255", "-8.5", "8.5", "-110", "-110")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-29 09:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-125", "190", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-29 09:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-225", "250", "-3.5", "3.5", "-100", "-120")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-29 21:45:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-125", "195", "-1.5", "1.5", "-105", "-110")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-29 21:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-220", "255", "-3.5", "3.5", "-100", "-120")
    insert_into_dynamodb("qwdq32e132e23dw323dq32dqd32d", "2023-09-30 09:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Bears", "Steelers",
                         "-110", "140", "-1.0", "1.0", "-100", "-100")
    insert_into_dynamodb("12lopo12vzva21nwmsa3212wswsq", "2023-09-30 09:51:11.670229", "2023-10-01T13:30:00Z",
                         "Barstool", "Chiefs", "Giants",
                         "-241", "255", "-3.0", "3.0", "-110", "-110")


def read_handler():
    # Initialize DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('')
    s3 = boto3.client('s3', region_name='us-east-1')
     # Query DynamoDB
    response = table.scan()
    items = response['Items']

    # Organize Data
    # Organize data by game_id and sort by timestamp
    organized_data = {}
    for item in items:
        game_id = item['GameID']
        bookmaker, timestamp_str = item['SortKey'].split('#')
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
        comTime = item['Game-Time']
        gametime = datetime.strptime(comTime, "%Y-%m-%dT%H:%M:%SZ")

        if game_id not in organized_data:
            organized_data[game_id] = []

        ##moneymaker
        if bookmaker == "DraftKings":
            organized_data[game_id].append({
                'Date': timestamp,
                'HomeTeam': item['HomeTeam'],
                'AwayTeam': item['AwayTeam'],
                'HMoneyline': item['HomeML'],
                'AMoneyline': item['AwayML'],
                'Bookmaker': bookmaker,
                'Game Time': str(gametime.month) + "/" + str(gametime.day) + "  " + fix_time(gametime.hour, gametime.minute)
                # str(gametime.hour) + " " + str(gametime.minute) #
            })

    for game_data in organized_data.values():
        game_data.sort(key=lambda x: x['Date'])

    # html time
    with open('index_template.html', 'r') as f:
        html_template = f.read()

    dynamic_html = ""

    for game_id, game_data in organized_data.items():
        dates = [record['Date'] for record in game_data]

        hmoneylines = [int(record['HMoneyline']) for record in game_data]
        amoneylines = [int(record['AMoneyline']) for record in game_data]

        plt.figure(figsize=(12, 6))
        plt.subplots_adjust(wspace=0.3)

        # Plot for Away Team
        plt.subplot(1, 2, 1)

        plt.plot(dates, amoneylines)
        plt.title(f"Moneyline Trend for the {game_data[0]['AwayTeam']}")
        plt.xlabel("Date")
        plt.ylabel("Moneyline")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        plt.gcf().autofmt_xdate()
        interval = calculate_interval(min(amoneylines), max(amoneylines))
        plt.yticks(range(min(amoneylines), max(amoneylines) + 1, interval))
        # set_y_axis_limits(min(amoneylines), max(amoneylines))
        # Plot for Home Team
        plt.subplot(1, 2, 2)
        plt.plot(dates, hmoneylines)
        plt.title(f"Moneyline Trend for the {game_data[0]['HomeTeam']}")
        plt.xlabel("Date")
        plt.ylabel("Moneyline")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        plt.gcf().autofmt_xdate()
        interval = calculate_interval(min(hmoneylines), max(hmoneylines))
        plt.yticks(range(min(hmoneylines), max(hmoneylines) + 1, interval))
        # set_y_axis_limits(min(hmoneylines), max(hmoneylines))

        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)

        # Upload to S3
        s3.put_object(Body=img_data.read(), Bucket='bucketname', Key=f"{game_id}_graph.png",
                      ContentType='image/png')

        # Clear the current plot for the next one
        plt.clf()
        away_team = game_data[0]['AwayTeam']
        home_team = game_data[0]['HomeTeam']
        gtime = game_data[0]['Game Time']

        # Append to HTML content
        dynamic_html += f"<h1> {away_team} vs {home_team} {gtime}</h1>"
        dynamic_html += f"<img src='http://bucketname.s3-website-us-east-1.amazonaws.com/{game_id}_graph.png' alt='Odds Graph'>"
        dynamic_html += "<ul><h3>Odds movement Full Log (Week)</h3>"
        for record in game_data:
            getDate = datetime.strptime(str(record['Date']), '%Y-%m-%d %H:%M:%S.%f')

            getTime = record['Game Time']
            dynamic_html += f"<li>Date:  {str(getDate.month) + '-' + str(getDate.day)}  |   {fix_time(getDate.hour, getDate.minute)} , {away_team} Moneyline:  {adj_odds(record['AMoneyline'])}, {home_team} Moneyline: {adj_odds(record['HMoneyline'])}  |  Bookmaker: {record['Bookmaker']}</li>"
        dynamic_html += "</ul>"

    final_html = html_template.replace("{dynamic_content}", dynamic_html)

    # Upload HTML content to S3
    s3.put_object(Body=final_html, Bucket='huff-live-odds-prod', Key='index.html', ContentType='text/html')
    s3.upload_file("styles.css", "huff-live-odds-prod", "styles.css")
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': final_html
    }


def calculate_interval(min_val, max_val):
    diff = max_val - min_val

    if diff <= 10:
        return 1
    elif diff <= 24:
        return 2
    elif diff <= 50:
        return 5
    elif diff <= 100:
        return 10
    elif diff <= 200:
        return 20
    elif diff <= 500:
        return 50
    else:
        return 100


def set_y_axis_limits(min_val, max_val):
    diff = max_val - min_val
    if diff < 150:
        mid_point = (max_val + min_val) // 2
        new_min = mid_point - 75
        new_max = mid_point + 75
        plt.ylim(new_min, new_max)
    else:
        plt.ylim(min_val, max_val)

def fix_time(h, m):
    if h > 12:
        gthour = h - 12
        gtmin = fix_minute(m) + " PM"
    elif h == 0:
        gthour = 12
        gtmin = fix_minute(m) + " AM"
    else:
        gthour = h
        gtmin = fix_minute(m) + " AM"
    return str(gthour) + ":" + gtmin


def fix_minute(m):
    if m == 0:
        return str(m) + "0"
    else:
        return str(m)


def adj_odds(odds):
    if int(odds) > 0:
        return " +" + str(odds)
    else:
        return str(odds)
