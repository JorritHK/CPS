package life.game.generator

import java.util.ArrayList
import life.game.gameOfLifeDSL.GameSpec
import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.Rule
import life.game.gameOfLifeDSL.Condition
import java.util.HashMap

class Util {
	def static HashMap<Consequence, ArrayList<Condition>> getRuleMap(GameSpec root) {
	var ruleMap = new HashMap<Consequence, ArrayList<Condition>>()
	ruleMap.put(Consequence.DEATH, new ArrayList<Condition>())
	ruleMap.put(Consequence.LIVE, new ArrayList<Condition>())
	ruleMap.put(Consequence.BORN, new ArrayList<Condition>())
	
	for (Rule r : root.rules.rules) {
		ruleMap.get(r.consequence).add(r.reason.condition)
	}
	return ruleMap;
	}
}