from screen import *

test_room_one = screen(title="room one\n")
test_room_two = screen(title="room two\n")

test_room_one.options = (option(display="room two",valid_actions={"goto":validaction(go_to_where=test_room_two)}),)
test_room_two.options = (option(display="room one",valid_actions={"goto":validaction(go_to_where=test_room_one)}),)