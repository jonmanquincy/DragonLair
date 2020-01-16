class TreeNode:

    def __init__(self, story_piece, chosen_index=None):
        self.story_piece = story_piece
        self.choices = []
        self.chosen_index = chosen_index

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in ["1", "2"]:
                print("Invalid choice. Try Again.")
            else:
                self.chosen_index = int(choice)
                self.chosen_index -= 1
                chosen_child = story_node.choices[self.chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child



current_fight = TreeNode("""
Thank goodness that slime didn't do you in!
But now you are faced with a choice.
Will you:
1) Travel over the mountain?
2) Travel under the mountain through the caves?
""")

the_mountains = TreeNode("""
You huff and puff, digging deep to climb this mountain.
Perhaps you have eaten a few too many pastries in the past few months?
As you ponder your diet decisions, you hear a noise.
A menacing Wyvern turns the corner; Big green wings a flappin', venomous saliva dripping from it's mouth,
and eyes that say it too has been thinking about it's diet. 
And you are on it.
""")
the_caverns = TreeNode("""
The caverns are as cold as they are dark.
Wondering how things underground manage to stay so wet; you hear a noise.
Rocks rumble and tumble to assemble a great Earth Golem in front of you.
It seems to like it's cave without you in it.
""")

current_fight.add_child(the_mountains)
current_fight.add_child(the_caverns)

