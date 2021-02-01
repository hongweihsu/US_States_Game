import turtle
import pandas

data = pandas.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = data.state.to_list()
guessed_states = []
exit_code = "Exit"

while len(guessed_states) < len(all_states):

    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} State Correct", prompt="What's another state's name")
    answer_state = answer_state.title()

    if answer_state == exit_code:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        header = ['Missed State']
        new_data.to_csv("states_missed.csv", header=header)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        x = data[data["state"] == answer_state]["x"]
        y = data[data["state"] == answer_state]["y"]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(answer_state)

screen.exitonclick()