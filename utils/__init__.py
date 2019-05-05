""" reusable python functions """
import pandas as pd
import requests
import datetime


def get_missing_dates(all_dates, actual_dates):
    """ get dates tht were not used in actual list """
    results = []
    for x in all_dates:
        match_in_list2 = None
        for y in actual_dates:
            if x.date() == y.date():
                match_in_list2 = y
                break

        if match_in_list2:
            results.append(match_in_list2)
        else:
            results.append(x)
    return [d for d in results if (d.second == 0 and d.minute == 0 and d.hour == 0)]


def fill_in_blanks(df, start, end):
    """ add missing dates with 0.0 transactions """
    missing_dates = get_missing_dates(get_full_dates(start, end),
                                      df['ds'].copy().tolist())
    new_df = pd.DataFrame.from_dict({"ds": missing_dates,
                                     "target": [0 for l in range(len(missing_dates))]})
    return pd.concat([df, new_df]).sort_values(by=['ds'])


def collect_data(start, end, category):
    url = "https://report.fatdataunicorn.com/admin/minimal_data?start={}&end={}".format(start, end)
    if category is not None:
        url += "&category={}".format(category)
    resp = requests.get(url=url, headers={"auth-user": "fedorinogore", "auth-pswd": "This01s0GooD"}).json()

    raw_dict = {"ds": [], "cat": [], "target": []}
    raw = json.loads(resp['Payload'])
    for item in raw:
        raw_dict["ds"].append(datetime.datetime.strptime(item['time'], "%Y-%m-%dT%H:%M:%S"))
        raw_dict["cat"].append(item['category'])
        raw_dict["target"].append(float(item['amount']))
    dates_list = []
    return pd.DataFrame.from_dict(raw_dict)


def get_full_dates(start, end, dates=False):
    """ Get all days list from start to end date """
    total_days = (end - start).days
    res = []
    for i in range(total_days):
        res.append(start + datetime.timedelta(days=i))
    if dates:
        return [r.date() for r in res]
    return res