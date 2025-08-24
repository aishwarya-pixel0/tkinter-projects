import turtle
import pandas
#resizing the image using pillow in pil(python imaging library)
from PIL import Image
from tkinter import messagebox
import winsound
img = Image.open("indian_map.gif")
new_img = img.resize((700,700))  # Resize to 200x200 pixels
screen = turtle.Screen()
# # Save the resized image
new_img.save("new_image.gif")
turtle.addshape("new_image.gif")
turtle.shape("new_image.gif")
screen.title("How well do you know India?")
data = pandas.read_csv("states_and_uts.csv")
#converting the states attribute in csv to list
all_states=data.state.to_list()
guessed_states=[]
unq_list = []
while len(guessed_states)<36:
    answer_state = screen.textinput(title=f"{len(unq_list)}/35 States and UT Correct",
                                    prompt="Name a State or UT of India")
    # print(answer_state)
    if answer_state is None:
        break

    answer_state = answer_state.title()
    #creates a csv with all the states the user has missed
    if answer_state=="Exit":
        messagebox.showinfo(title="Score",message=f"Your score is {len(unq_list)}/35 ")
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_missed.csv")
        break
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state==answer_state]
        guessed_states.append(answer_state)
        unq_list = list(set(guessed_states))

        #accessing single item in the pandas series
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
        winsound.PlaySound("correct.wav", winsound.SND_FILENAME)
    else:
        winsound.PlaySound("error.wav", winsound.SND_FILENAME)


# #got the coordinates of each state and ut
# def get_mouse_click_coor(x,y):
#         print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()



