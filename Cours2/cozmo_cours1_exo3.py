import cozmo


def interaction(robot:cozmo.robot.Robot):
    robot.say_text('salut, je suis Cozmo. Et toi?').wait_for_completed()
    nom = input('entre ton nom:')
    robot.say_text('bonjour ' + nom).wait_for_completed()


cozmo.run_program(interaction)

