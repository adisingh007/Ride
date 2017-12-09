# Ride
---
##### Created by - Aditya Singh - 09/12/2017
##### Mail me at: [aditya.sin@media.net](mailto:aditya.sin@media.net)

This lets you book a cab from the http://drops/ interface right from your terminal. :D  
Just set your credentials in `drop-details.json` and you are good to go.  
  
The required details are:  
  
```
src: 1 for Mumbai-Plex / 2 for Mumbai-Seepz
uname: your AD username here
pwd: your password
location: where do u wanna book your ride for
time: the time you wanna book your ride at
```  
  
## Note:
Time and location should be one of those shown on the http://drops/ interface.
  
All these details need to be set once and that is it. Just make sure you have `python 3` installed.  
  
Open up your terminal and type:  
  
````
cd /location/to/the/app/directory  
python ride.py  
````

You can also set a `CRON` for this. :D

