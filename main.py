import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data)

data_states_list = data["state"].to_list()
data_x_list = data["x"].to_list()
# print(data_x_list)
data_y_list = data["y"].to_list()
# print(data_states_list)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in data_states_list:
        if answer_state in guessed_states:
            screen.textinput(title="Warning!", prompt="This answer had already guessed. Please guess again.")
        else:
            guessed_states.append(answer_state)
            index = data_states_list.index(answer_state)
            # print(index)
            x = data_x_list[index]
            y = data_y_list[index]
            state_title = turtle.Turtle()
            state_title.penup()
            state_title.hideturtle()
            state_title.goto(x, y)
            state_title.write(answer_state)
    elif answer_state == "Exit":
        missing_states_exit = [state for state in data_states_list if state not in guessed_states]
        new_data_exit = pandas.DataFrame(missing_states_exit)
        new_data_exit.to_csv("states_to_learn_after_exit.csv")
        break
    elif answer_state != data_states_list:
        # missing_states = []
        # for state in data_states_list:
        # if state not in guessed_states:
        # missing_states.append(state)
        missing_states = [state for state in data_states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


# screen.exitonclick()
