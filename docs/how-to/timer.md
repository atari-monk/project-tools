# Ubuntu Pomodoro Timer

## 1. Test it — 5 seconds

### Start timer

```bash
(s=$(date '+%Y-%m-%d %H:%M:%S'); echo "Start: $s" >> /tmp/timer.log; sleep 5s; e=$(date '+%Y-%m-%d %H:%M:%S'); echo "End: $e" >> /tmp/timer.log; notify-send "⏰ Timer finished!" "5 seconds are up!"; paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga) >/dev/null 2>&1 & disown
```

### Read timestamps

```bash
cat /tmp/timer.log
```

### Delete log

```bash
rm /tmp/timer.log
```

### Clear log without deleting the file

```bash
> /tmp/timer.log
```

For **25 minutes**, just change `sleep 5s` to `sleep 25m`.

```bash
(s=$(date '+%Y-%m-%d %H:%M:%S'); echo "Start: $s" >> /tmp/timer.log; sleep 25m; e=$(date '+%Y-%m-%d %H:%M:%S'); echo "End: $e" >> /tmp/timer.log; notify-send "⏰ Timer finished!" "25 minutes are up!"; paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga) >/dev/null 2>&1 & disown
```