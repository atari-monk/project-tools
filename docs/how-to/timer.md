# Ubuntu Pomodoro Timer

## 1. Test it — 5 seconds

Copy and run this directly in the terminal:

```bash
(sleep 5s; notify-send "⏰ Timer finished!" "5 seconds are up!"; paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga) &
```

You should immediately get your terminal prompt back. After 5 seconds, you'll get a notification and sound.

## 2. Run a 25-minute Pomodoro

```bash
(sleep 25m; notify-send "⏰ Pomodoro finished!" "25 minutes are up!"; paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga) &
```

The `&` makes the timer run in the background.

## 3. Python wrapper

Create `pomodoro.py`:

```python
import sys
import subprocess

duration = sys.argv[1] if len(sys.argv) > 1 else "25m"

cmd = (
    f'(sleep {duration}; '
    f'notify-send "⏰ Pomodoro finished!" "{duration} is up!"; '
    f'paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga) &'
)

subprocess.Popen(cmd, shell=True)

print(f"Pomodoro started: {duration}")
```

### Test with 5 seconds

```bash
python3 pomodoro.py 5s
```

### Normal Pomodoro

```bash
python3 pomodoro.py 25m
```

Other examples:

```bash
python3 pomodoro.py 5m
python3 pomodoro.py 30m
python3 pomodoro.py 1h
```

The Python command returns immediately while the timer continues running in the background.
