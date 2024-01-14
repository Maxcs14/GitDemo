import turtle, pandas

#turtle screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read csv data
data = pandas.read_csv("50_states.csv")

#convert csv data to list
all_states = data.state.to_list()

#declared guess states array
guess_states = []

#count the array len
while len(guess_states) < 50:
    #declare input
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
#condition for missing states
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

#condition for guessed states
    if answer_state in all_states and answer_state not in guess_states:
        t = turtle.Turtle()
        guess_states.append(answer_state)
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(str(answer_state), font=("Calibri", 11, "normal"))