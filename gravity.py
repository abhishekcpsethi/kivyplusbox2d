from Box2D.examples.framework import Framework
from Box2D import *


class GravityEffects(Framework):
    def __init__(self):
        super(GravityEffects, self).__init__()
        gravity_val = b2Vec2(0,-10)
        self.world.gravity = gravity_val
        self.world.CreateBody(shapes=b2LoopShape(
            vertices=[(20, 0), (20, 40), (-20, 40), (-20, 0)]
        ))
        circle = b2FixtureDef(
            shape=b2CircleShape(radius=3), density=1,
            friction=1.0, restitution=0.5
        )
        self.world.CreateBody(
            type=b2_dynamicBody, position=b2Vec2(0, 30),
            fixtures=circle
        )

    def Step(self, settings):
        super(GravityEffects, self).Step(settings)


if __name__ == '__main__':
    GravityEffects().run()