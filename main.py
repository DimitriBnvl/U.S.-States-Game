import turtle
import pandas
from mapping import Map

#----------------TURTLE MODULE----------------#
screen = turtle.Screen()
mapping = Map()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#---------------PANDAS MODULE---------------#
data = pandas.read_csv("50_states.csv")

#-----------------GAME DATA-----------------#
states = data.state.to_list()
x_cords = data.x.to_list()
y_cords = data.y.to_list()

#-----------------GAME BRAIN-----------------#
answered_states = []
prompt = "Guess the state"
while len(answered_states) < 50:
    answer_state = screen.textinput(title=prompt, prompt="Enter a state's name: ").title()
    if answer_state == "Exit":
        states_to_learn = [s for s in states if s not in answered_states]
        series = pandas.Series(states_to_learn)
        series.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        state_num = states.index(answer_state)
        mapping.correct_answer(x_cords[state_num], y_cords[state_num], answer_state)

        answered_states.append(answer_state)
        score = len(answered_states)
        prompt = f"{score} / 50 Correct States."