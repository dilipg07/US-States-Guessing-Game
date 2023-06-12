import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

gussed_states = []
while len(gussed_states) <50:
    answer = screen.textinput(title= f"{len(gussed_states)}/50 States correct", prompt="What's another state's name")
    answer = answer.title()
    data = pd.read_csv("50_states.csv")
    if answer == "Exit":
        non_gussed_states = []
        for x in list(data.state):
            if x not in gussed_states:
                non_gussed_states.append(x)
        non = pd.DataFrame(non_gussed_states)
        non.to_csv("states_to_learn.csv")
        break
    if  answer in list(data.state):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)
        gussed_states.append(answer)