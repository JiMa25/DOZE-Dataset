import ai2thor.controller
from ai2thor.controller import Controller
import time

def rotate_left(controller, degrees=90, steps=10, step_delay=0.05):
    step_size = degrees / steps
    for _ in range(steps):
        controller.step("RotateLeft", degrees=step_size)
        time.sleep(step_delay)

def rotate_right(controller, degrees=90, steps=10, step_delay=0.05):
    step_size = degrees / steps
    for _ in range(steps):
        controller.step("RotateRight", degrees=step_size)
        time.sleep(step_delay)

def move_ahead(controller, meters, step_delay=0.05):
    steps = int(meters * 4) 
    for _ in range(steps):
        controller.step("MoveAhead")
        time.sleep(step_delay)

controller = Controller(
    agentMode="default",
    visibilityDistance=1.5,
    gridSize=0.1,
    fieldOfView=90,
    local_executable_path = "../dynamic_fixed/DOZE_dynamic_fixed_3.x86_64",
    width=1920,
    height=1080
)

controller.step(
    action="LookDown",
    degrees=30
)
commands = "2 R 11 R 8 R 11 R 9 L 7 L 3 R 10 L 1 L 5 R 7"

# Split the command string into a single command
command_list = commands.split()


for command in command_list:
    if command.isdigit():
        move_ahead(controller, int(command) * 0.75)
    elif command == 'R':
        rotate_right(controller)
    elif command == 'L':
        rotate_left(controller)
