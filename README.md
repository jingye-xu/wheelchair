

## Robot Web RESTful API

### Camera

#### Camera up

URL:  
http://192.168.0.250:8080/?action=command&command=cam_up_up  
Method: GET

#### Camera down

URL:  
http://192.168.0.250:8080/?action=command&command=cam_down_up  
Method: GET

#### Camera left

URL:  
http://192.168.0.250:8080/?action=command&command=cam_left_up  
Method: GET

#### Camera right

URL:  
http://192.168.0.250:8080/?action=command&command=cam_right_up  
Method: GET

#### Camera stop

URL:  
http://192.168.0.250:8080/?action=command&command=cam_stop_up  
Method: GET

### Motor

#### Move forward

URL:  
http://192.168.0.250:8080/?action=command&command=move_command&value=655360  
Method: GET
```
Some valid values:
65536, 655360, 6553600  
  |       |       |  
slow   medium    fast  
```

#### Move backward

URL:  
http://192.168.0.250:8080/?action=command&command=move_command&value=537575426  
Method: GET

```
Some valid values:
536903680, 537575426, 548339722
    |          |          |  
  slow      medium       fast 
```

#### Turn left

URL:  
http://192.168.0.250:8080/?action=command&command=move_command&value=65566  
Method: GET

```
Some valid values
10, 65566, 98429
 |    |      |  
slow medium fast 
```

#### Turn right

URL:  
http://192.168.0.250:8080/?action=command&command=move_command&value=114712  
Method: GET

```
Some valid values
81929, 114712, 536985728
  |       |        |  
slow   medium     fast 
```

#### Stop motor

URL:
http://192.168.0.250:8080/?action=command&command=move_command&value=0  
Method: GET
