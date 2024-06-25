class DecisionNode:
    def __init__(self, question, yes_branch=None, no_branch=None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch

def build_decision_tree():
    leaf1 = DecisionNode("It's a sunny day. Enjoy your time!")
    leaf2 = DecisionNode("Take an umbrella with you.")
    leaf3 = DecisionNode("Have a great day at home!")
    leaf4 = DecisionNode("Do you have any indoor activities planned?", leaf3, leaf2)

    root = DecisionNode("Is it raining?", leaf4, leaf1)
    return root

def ask_question(node):
    if node.yes_branch is None and node.no_branch is None:
        print(node.question)
        return
    
    answer = input(node.question + " (yes/no): ").strip().lower()
    if answer == 'yes':
        ask_question(node.yes_branch)
    elif answer == 'no':
        ask_question(node.no_branch)
    else:
        print("Please answer with 'yes' or 'no'.")
        ask_question(node)

# Construindo e executando o chatbot
decision_tree = build_decision_tree()
ask_question(decision_tree)
