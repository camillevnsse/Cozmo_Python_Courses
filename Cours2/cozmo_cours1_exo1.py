import cozmo


def my_program(robot:cozmo.robot.Robot):
    robot.say_text('bonjour').wait_for_completed()
    robot.say_text('ça va?').wait_for_completed()


cozmo.run_program(my_program)

