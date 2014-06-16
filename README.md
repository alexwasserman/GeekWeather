GeekWeather
===========

Python script for pulling [ForeCast.io] weather information.

*Requirements*
  - Python

*Description*

This is a quick update to a wrapper from [ZeevG] using [climacons] from Adam Whitcroft

Forecast.io is a great weather service offering a forecast that's amazingly accurate. The data is available for free using their [API] (1000 hits a day). I used the wrapper above to create a little python script to pull in some forecast data and show the appropriate icon on my desktop.

You'll need to open up the GeekWeather.py script to put in your own APIKEY and location.  The key in the file is an example, and won't work.

Unzip and run GeekWeath.py, as long as the icons folder and and forecastio.py exist it'll be fine.

Version
----
1.0

Tech
-----------
GeekWeather uses:
 * Forecast.IO API
 * Python

Script usage
--------------

```sh
$./geekWeather.py
Right Now:            Clear
Next Hour:            None
Next 24 Hours:        Partly cloudy in the afternoon.
Next 7 Days:          None
```

License
-------

MIT

[ForeCast.io]: http://forecast.io/
[API]: https://developer.forecast.io/
[ZeevG]: https://github.com/ZeevG/python-forcast.io
[Climacons]: http://adamwhitcroft.com/climacons
