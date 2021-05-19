# Credit to the J! Archive (https://j-archive.com/) for the questions, and Jeopardy! for the questions, name, and idea. 
import random
from brython_graphics import *
def create_board(completed):
    board_rect = Rectangle(get_width(), get_height())
    board_rect.set_position(0, 0)
    board_rect.set_color(Color.blue)
    add(board_rect)
    dollars = ["$200", "$400", "$600", "$800", "$1000"]
    for i in range(5):
        line = Line(0, (i+1)*get_height()/6, get_width(), (i+1)*get_height()/6)
        line.set_color(Color.black)
        add(line)
    for i in range(5):
        line = Line((i+1)*get_width()/6, 0, (i+1)*get_width()/6, get_height())
        line.set_color(Color.black)
        add(line)
    for i in range(6):
        for j in range(5):
            if str(i) + str(j) not in completed:
                dollar = Text(dollars[j])
                dollar.set_color(Color.yellow)
                if len(dollars[j]) > 4:
                    dollar.set_font("25pt Helvetica")
                    dollar.set_position(i*get_width()/6+8, (j+2)*get_height()/6-25)
                else:
                    dollar.set_font("30pt Helvetica")
                    dollar.set_position(i*get_width()/6+10, (j+2)*get_height()/6-25)
                add(dollar)
def categories():
    category_choices = ["Before and After", "World Leaders", "World War II", "US Leaders", "Abbrev.", "Airport Codes", "The Oscars", "TV", "Sports", "Elections", "Video Games", "Borders", "The “U” Ending", "Game Shows", "History BC"]
    final_cats = []
    for i in range(6):
        cat = random.choice(category_choices)
        category_choices.remove(cat)
        final_cats.append(cat)
    for i in range(6):
        category=final_cats[i].split()
        if final_cats[i] == "World War II":
            category=["World", "War II"]
        elif final_cats[i] == "The Royal Family":
            category=["The Royal", "Family"]
        elif final_cats[i] == "Before and After":
            category=["Before", "and After"]
        elif final_cats[i] == "The “U” Ending":
            category=["The “U”", "Ending"]
        if len(category) == 1:
            dollar=Text(category[0].center(10))
            dollar.set_position(i*get_width()/6, get_height()/6-25)
            dollar.set_color(Color.white)
            dollar.set_font("20pt Arial")
            add(dollar)
        else:
            for j in range(len(category)):
                dollar=Text(category[j].center(10))
                dollar.set_position(i*get_width()/6, (j*30+30))
                dollar.set_color(Color.white)
                dollar.set_font("20pt Arial")
                add(dollar)
    return final_cats
def show_question(x, y):
    for i in range(6):
        if (get_width()*i)/6 < x:
            column = i
    for i in range(1, 6):
        if (get_height()*i)/6 < y:
            row = i - 1
    print(str(column)+str(row))

before_and_after = None
set_size(650, 446.875)
create_board([])
categories = categories()
add_mouse_click_handler(show_question)