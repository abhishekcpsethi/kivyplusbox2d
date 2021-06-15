from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Ellipse
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from gravity import GravityEffects


class GravityEffectApp(App):
    pass


class MainLayoutForPyGame(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_submit(self,gravity):
        gravity_effect = GravityEffects(float(gravity))
        gravity_effect.run()




"""
Writing code for using kivy only for demonstration
"""
class MainLayoutKivy(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.gravity_for_experiment = -1
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.count = 0


    def on_submit(self,gravityVal,boxlayout):
        print("submit button pressed")

        try:
            if (int(gravityVal) < 0):
                print("invalid values for g")
                return
            else:
                self.count += 1
                if (self.count == 1):
                    with boxlayout.canvas:
                        self.gravity_for_experiment = gravityVal
                        self.vy = dp(gravityVal)
                        ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
                        self.ball = ball
                        Clock.schedule_interval(self.updateWithKivy,1/60)
                else:
                    print("simulation already in progress")

        except ValueError:
            print("gravity not a numeric")
            return


    def updateWithKivy(self, dt):
        x, y = self.ball.pos
        panel_width = self.width - dp(175)
        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > panel_width:
            x = panel_width -self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)


GravityEffectApp().run()

