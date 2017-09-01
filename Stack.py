Stack = []
top = -1
def push():
	print "Enter an element to insert into stack:"
	Stack.append(int(raw_input()))
def pop():
	Stack.pop()
def display():
	print Stack
while(True):
	print "1.Insert an element into stack"
	print "2.Pop operation"
	print "3.Display Stack"
	i = raw_input()
	if i == "1":
		push();
	elif i == "2":
		if length(Stack) == 0:
			print "No elements to remove from the stack"
		else:
			pop();
	elif i == "3":
		display();
	else:
		print "Choose a correct option"