package persons.tasks.generator

import java.util.ArrayList
import java.util.List
import persons.tasks.taskDSL.Action
import persons.tasks.taskDSL.Planning
import persons.tasks.taskDSL.Task
import persons.tasks.taskDSL.Person

class Auxiliary {
	def static List<Action> getActions(Planning root) {
		var List<Action> actionlist = new ArrayList<Action>()
			for (Task t : root.tasks){
			actionlist.add(t.action)
			}
		return actionlist;
	}
	
	def static Planning getPersonPlanning(Person person) {
		return person.eContainer() as Planning
	}
}