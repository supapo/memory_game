# implementation of card game - Memory
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    import random



card_shit = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
shit = random.shuffle(card_shit)
print(card_shit)
exposed = False
new_shit = 'green'
shimi = []

# helper function to initialize globals
def new_game():
    pass  


# define event handlers
def mouseclick(pos):
    global exposed, new_shit, upper_left, upper_right, lower_right, lower_left
    marshmallow = pos[0] //50
    for i in range(len(card_shit)):
        if i == marshmallow:
            exposed = True
            shimi = marshmallow
            shimi.append()
            print(card_shit[i])
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    posi = 14
    upper_left = [5, 5]
    upper_right = [45, 5]
    lower_right = [45, 95]
    lower_left = [5, 95]    
    for i in card_shit:
        canvas.draw_text(str(i), [posi, 70], 55, 'green')
        posi += 50
        canvas.draw_polygon([upper_left, upper_right, lower_right, lower_left], 8, 'green', new_shit)
        upper_right[0] += 50
        lower_right[0] += 50
        upper_left[0] += 50
        lower_left[0] += 50

def main():
    # create frame and add a button and labels
    frame = simplegui.create_frame("Memory", 800, 100)
    frame.add_button("Reset", new_game)
    label = frame.add_label("Turns = 0")

    # register event handlers
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)

    # get things rolling
    new_game()
    frame.start()


# Always remember to review the grading rubric3

if __name__ == "__main__":
    main()