from p5 import *

balls = []
count = 0

def setup():
  createCanvas(windowWidth, windowHeight)
  textAlign(CENTER, CENTER)
  colorMode(HSB)
  createBalls()


def draw():
  global count
  background("black")
  for ball in balls:
    if ball.alive:
      if keyIsDown(ball.letter):
        count += 1
        ball.alive = 0
        strokeWeight(5)
        stroke("red")
        line(ball.x, ball.y, width / 2, 50)
      ball.show()
    ball.move()  
  fill("red")
  triangle(width / 2, 50, width / 2 - 20, 0, width / 2 + 20, 0)
  text(("Hits : " + str(count)), width - 100, height - 50)


class Ball:
  def __init__(self, x, y, speed, letter, col):
    self.x = x
    self.y = y    
    self.speed = speed
    self.letter = letter
    self.alive = 1
    self.color = col

  def show(self):
    fill(self.color, 100, 100, 0.3)  
    noStroke()
    circle(self.x, self.y, 100)
    fill("white")
    textSize(30)
    text(chr(self.letter), self.x, self.y)

  def move(self): 
    self.y += self.speed
    if self.y < - 50:
      self.y = random(height, height + 50)
      self.letter = floor(random(65, 91))
      self.alive = 1


def createBalls():
  for i in range(10):
    ball = Ball(
      random(50, width - 50),
      -random(50, height / 2),
      random(-5, -1),
      floor(random(65, 91)),
      random(256))  
    balls.append(ball)