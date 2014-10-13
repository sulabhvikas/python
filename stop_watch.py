# template for "Stopwatch: The Game"
import simplegui

# define global variables
watch_counter = 0
tenth_sec = 0
success_attempt = 0
total_attempts = 0
watch_position = [180, 110]
score_position = [325, 45]
width = 400
height = 200
interval = 100

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenth_sec
    min = t // 600
    ten_sec = (t // 100) % 6
    unit_sec = (t // 10) % 10
    tenth_sec = t % 10
    # string representation of the formatted time
    stop_watch = str(min) + ':' + str(ten_sec) + str(unit_sec) + '.' + str(tenth_sec)
    return stop_watch

def format_score(attempt, total):
    return str(success_attempt) + '/' + str(total_attempts)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    """ starts stop watch"""
    timer.start()

def stop():
    """ stop stop watch"""
    global success_attempt, total_attempts, score
    if (timer.is_running()):	# make sure timer is ON
        if ( tenth_sec == 0 ):  # check for whole sec
            success_attempt += 1
        total_attempts += 1
    #score = str(success_attempt) + '/' + str(total_attempts)
    timer.stop()

def reset():
    """ reset stop watch"""
    global watch_counter, success_attempt, total_attempts, score
    watch_counter = 0
    success_attempt = 0
    total_attempts = 0
    #score = str(success_attempt) + '/' + str(total_attempts)
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def tick():
    global watch_counter
    watch_counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(watch_counter), watch_position, 36, "White")
    canvas.draw_text(format_score(success_attempt, total_attempts), score_position, 35, "Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch", width, height)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
