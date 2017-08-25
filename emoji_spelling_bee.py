emojis = {'zzz', 's', '8', '777', '@', '9', 'm', 'n', 'id', 'off','vs', 'a', 'b', 'ab', 'cl', 'o', 'sos', 'x', 'loo', 'y', 'm', 'atm', 'wc', 'p', 'ng', 'ok', 'cool', 'new', 'free', 'up', 'i', 'abc',
'abcd', 'w', 't', 's', 'sy', 'c', 'r', 'tm', 'end', 'back', 'on', 'top', 'oni', 'soon', 'v'}
#emojis = {'back', 'on' ,'top'}
NFA = dict()
for token in emojis:
	state = NFA
	for letter in token:
		if letter not in state:
			state[letter] = dict()
		state = state[letter]
	state[None] = NFA
	#assert NFA is state[None]

def run_NFA(NFA, word):
	states = [NFA]
	for letter in word:
		new_states = []
		for state in states:
			#assert None not in state, state
			if letter in state:
				new_states.append(state[letter])
		states = new_states[:]
		#print(len(states))
		#new_states
		for state in states:
			#print(id(state))
			while None in state:
				state = state[None]
			new_states.append(state)
		#print([id(state) for state in new_states])
		states = new_states
	#print([id(state) for state in new_states])
	return any(state is NFA for state in states)

with open('words.txt') as f:
	wordlist = [word.lower() for word in f.read().split()]

emojiable_words = []

for word in wordlist:
	if run_NFA(NFA, word):
		print(word)
		emojiable_words.append(word)