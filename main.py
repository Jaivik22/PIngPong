# Create the app
# Create the game
# build the game
# run the game

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
# from CustomModules import CustomGraphics
from kivy.clock import Clock
from kivy.core.image import Image
from random import randint
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Builder.load_file('pong.kv')
Window.clearcolor = (76/255.0,187/255.0,23/255.0,1)
class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            ball.velocity_y *= -1



class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    # latst position = current_velocity + current_position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# update:moving the ball by calling move() and other stuff
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))
    

    def update(self,dt):
        self.ball.move()

        # bounce of top and bottom
        if (self.ball.y < 0) or (self.ball.y > self.height-25):
            self.ball.velocity_y *=-1.0

        #bounce of left and right
        if (self.ball.x < 0) or (self.ball.x > self.width-25):
            self.ball.velocity_x *=-1.0


        # player_1 increse the score
        if self.ball.y < 0 :
            self.player1.score+=1
         # player_2 increse the score
        if self.ball.y > self.height-25:
            self.player2.score += 1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.y < self.height / 1/2  -50 and touch.x < self.width:
            self.player1.center_y = touch.y
            self.player1.center_x = touch.x


        if touch.y > self.height * 1/2 +50  and touch.x < self.width:
            self.player2.center_x = touch.x
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):

        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/120.0)
        # CustomGraphics.SetBG(layout, bg_color=[1, 0, 0, 1])
        return game

PongApp().run()