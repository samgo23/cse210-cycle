from game.scripting.action import Action


class MoveActorsAction(Action):
    """ An update action that handles interactions between the actors.
    
    The responsibility of MoveActorsAction is to handle the movemnet of cycle.

    Attributes:
        execute (self, cast, script): moves actors on terminal.
    """
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()