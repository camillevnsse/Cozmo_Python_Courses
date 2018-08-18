import cozmo


def my_program(robot:cozmo.robot.Robot):
    robot.say_text('bonjour').wait_for_completed()
    robot.say_text('changement de voix', use_cozmo_voice=False).wait_for_completed()
    robot.say_text('je parle plus aigu', voice_pitch=1.0).wait_for_completed()
    robot.say_text('plus grave', voice_pitch=-1.0).wait_for_completed()


cozmo.run_program(my_program)

