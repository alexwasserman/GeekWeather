#!/usr/bin/python

from forecastio import Forecastio
import datetime
import os

def main():
    forecast = Forecastio("dada3cbcc93a16056f865e34daec507a")

# Get Current weather
    result_current = forecast.load_forecast(40.4017,-74.0368,
                                   time=datetime.datetime.now(),units="si")

# Process weather data
    if result_current['success'] is True:
        byCurrent = forecast.get_currently()
        byMinute = forecast.get_minutely()
        byHour = forecast.get_hourly()
        byDay = forecast.get_daily()

    else:
        print "A problem occured communicating with the Forecast.io API"

# Print what we want, lining stuff up neatly
    print "Right Now: %-10s %s" % ("", byCurrent.summary)
    print "Next Hour: %-10s %s" % ("", byMinute.summary)
    print "Next 24 Hours: %-6s %s"  % ("", byHour.summary)
    print "Next 7 Days: %-8s %s" % ("", byDay.summary)


# Get us to our script folder so the link is created in the right place
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

# Get our icon and create the link. Go my most specific weather conditions.

    iconimg =  "None"
    if str(byCurrent.icon) == "None":
        if str(byMinute.icon) == "None":
            if str(byHour.icon) == "None":
                iconimg = byDay.icon
            else:
                iconimg = byHour.icon
        else:
            iconimg = str(byMinute.icon)
    else:
        iconimg = str(byCurrent.icon)

# Unlink the current image so it can be relinked or updated
    os.unlink("current.png")

    if iconimg == "clear-day":
        os.symlink("icons/Sun.png","current.png")

    if iconimg == "clear":
        os.symlink("icons/Sun.png","current.png")

    if iconimg == 'clear-night':
        os.symlink("icons/Moon.png","current.png")

    if iconimg == "rain":
        os.symlink("icons/Rain.png","current.png")

    if iconimg == 'snow':
        os.symlink("icons/Snow.png","current.png")

    if iconimg == 'sleet':
        os.symlink("icons/Sleet.png","current.png")

    if iconimg == 'wind':
        os.symlink("icons/Wind.png","current.png")

    if iconimg == 'fog':
        os.symlink("icons/Fog.png","current.png")

    if iconimg == "cloudy":
        os.symlink("icons/Cloud.png","current.png")

    if iconimg == 'partly-cloudy-day':
        os.symlink("icons/Cloud-Day.png","current.png")

    if iconimg == 'partly-cloudy-night':
        os.symlink("icons/Cloud-Night.png","current.png")

if __name__ == "__main__":
    main()
