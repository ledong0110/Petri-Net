from PetriNetModel import PetriNet

if __name__ == "__main__":
	#Here is the sample construct Petri net (The sample image in the output_image folder, or in page 21 of assignment)
	dic = {
		"Places":{	
					"a":2,
					"b":2,
					"c":0,
					"d":0,
					"out":0
				 },
		"Transitions": {
						"t1":{"in": ["a"], "out": ["out"]}, 
						"t2":{"in": ["b"],"out": ["out"]},
						"t3":{"in": ["c"], "out": ["out"]},
						"t4": {"in": ["d"], "out": ["out"]}
						},
		"Fire": 10

	}
	#Add construction to Petri net
	u = PetriNet(dic)
	#Start modelling
	u.modelize()
	#Run it!!!!!!!!
	u.run()
	print("The number of reachable markings from initial marking are " + str(u.count_reachable_marking()))
	print("The terminal markings are:")
	print( u.find_all_deadlocks())
	print("The number of Transitions in Transitions System: " + str(u.number_of_trans_in_TS()))