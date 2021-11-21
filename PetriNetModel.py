#Define place
class Place:
	def __init__(self, tokens, label):
		self.tokens = tokens
		self.label = label

#Define arcs
class ArcProperty:
	def __init__(self, place, amount=1):
		self.place = place
		self.amount = amount
		
		#Define preset of transition
class InArc(ArcProperty):
	def activate(self):
		self.place.tokens -= self.amount

	def enoughtToken(self):
		return self.place.tokens >= self.amount

		#Define postset of transition
class OutArc(ArcProperty):
	def activate(self):
		# print(self.place)
		self.place.tokens += self.amount

#Definre transition
class Transitions:
	def __init__(self, label, in_arc, out_arc):
		self.label = label
		self.in_arc = set(in_arc)
		self.arcs = self.in_arc.union(out_arc)
	
	def check_token(self):
		return all(a.enoughtToken() for a in self.in_arc)

	def fire(self):
		trigger = self.check_token()
		if trigger:
			for arc in self.arcs:
				arc.activate()

		return trigger
#Define Petri net   
class PetriNet:
	def __init__(self, script):
		self.script = script
		self.set_of_trans = []
		self.model = {}
		self.model_check = 0
		self.places = 0
		self.firing_list = []
		self.list_reachable_marking = []
		self.initial_marking = []
		self.deadlocks = []
		self.count_trans = 0

	def modelize(self):
		self.model_check = 1
		ts = {}
		places = self.script['Places']
		place_keys = list(places.keys())
		self.places = [Place(places[place], place) for place in place_keys]
		transitions = self.script['Transitions']
		for trans in transitions:
			label_trans = str(trans)

			pre = transitions[trans]["in"]
			pos = transitions[trans]["out"]
			preset = []
			postset = []
			# print(label_trans + ": ")
			for p in range(len(place_keys)):
				am = pre.count(place_keys[p])
				if am != 0:
					# print("In arc: " + self.places[p].label + " Amount tokens: " + str(am))
					preset.append(InArc(self.places[p],am))
			for p in range(len(place_keys)):
				am = pos.count(place_keys[p])
				if am != 0:
					# print("Out arc: " + self.places[p].label + " Amount tokens: " + str(am))
					postset.append(OutArc(self.places[p],am))
			ts[label_trans] = Transitions(label_trans, preset, postset)
		self.model = ts
		self.number_of_fires = self.script['Fire']
		self.set_of_trans = list(self.model.keys())
		self.initial_marking = [p.tokens for p in self.places]

	def deadlock(self):
		flag = True
		for ts in self.model.values():
			if ts.check_token():
				flag = False
		return flag
	def run(self):
		from random import choice
		if not (self.model_check):
			print("You haven't modelling yet !!!\nTry with object.model() after that object.run()")
			return
		self.firing_list = [choice(list(self.model.keys())) for _ in range(self.number_of_fires)]
		print(("Here is firing sequence from %d random transitions: " + "-->".join(self.firing_list))%(self.number_of_fires))
		print("Order places: {}".format([p.label for p in self.places]))
		print("Initial Marking: {}".format([p.tokens for p in self.places]))
		print("---------------------------------------------------------")
		for i in self.firing_list:
			ts = self.model[i]
			if ts.fire():
				print(str(i) + " fired !")
				print("The reachable marking now is: {}".format([p.tokens for p in self.places]))
				print("---------------------------------------------------------")
			else:
				print(str(i)+" is not enabled !")
				print("---------------------------------------------------------")

		if (self.deadlock()):
			print("The Petri net meets deadlock at marking: {}".format([p.tokens for p in self.places]))
		else:
			print("Final Marking: {}".format([p.tokens for p in self.places]))
		k = 0
		for p in self.places:
			p.tokens = int(self.initial_marking[k])
			k = k + 1

	def dfs(self, marking, list_dead):
		self.list_reachable_marking.append(marking)
		if not self.deadlock():
			for i in self.set_of_trans:
				ts = self.model[i]
				if (ts.check_token()):
					ts.fire()
					self.count_trans+=1
					u = [p.tokens for p in self.places]
					if u not in self.list_reachable_marking:
						self.dfs(u, list_dead)
					k = 0
					for p in self.places:
						p.tokens = int(marking[k])
						k+=1
		else:
			list_dead.append(marking)


	def unique(self, seq):
		ref = [] 
		for i in seq:
			if i not in ref: 
				ref.append(i)
		return ref

	def count_reachable_marking(self, list_dead=[]):
		self.list_reachable_marking.clear()
		marking = [p.tokens for p in self.places]
		self.count_trans = 0
		self.dfs(marking, list_dead)
		return len(self.list_reachable_marking)

	def find_all_deadlocks(self):
		self.deadlocks.clear()
		list_dead = []
		self.count_reachable_marking(list_dead)
		self.deadlocks = self.unique(list_dead)
		return self.deadlocks

	def number_of_trans_in_TS(self):
		self.count_reachable_marking()
		return self.count_trans