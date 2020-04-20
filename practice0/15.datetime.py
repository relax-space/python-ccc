import datetime


def get_yestoday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yestoday = today - oneday
    return yestoday


print("昨天日期为：", get_yestoday())
