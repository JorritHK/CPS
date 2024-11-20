package life.game.generator

import java.util.ArrayList
import life.game.gameOfLifeDSL.GameSpec
import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.Rule
import life.game.gameOfLifeDSL.Condition
import life.game.gameOfLifeDSL.Operator
import java.util.HashMap

class Util {
	def static HashMap<Consequence, ArrayList<Condition>> getRuleMap(GameSpec root) {
		var ruleMap = new HashMap<Consequence, ArrayList<Condition>>()
		ruleMap.put(Consequence.DEATH, new ArrayList<Condition>())
		ruleMap.put(Consequence.SURVIVAL, new ArrayList<Condition>())
		ruleMap.put(Consequence.BORN, new ArrayList<Condition>())
		
		for (Rule r : root.rules.rules) {
			ruleMap.get(r.consequence).add(r.reason.condition)
		}
		return ruleMap;
	}
	
	def static String getOperatorStr(Operator op) {
		if (op.LARGER !== null) return op.LARGER
		if (op.SMALLER !== null) return op.SMALLER
		if (op.EQUAL !== null) return op.EQUAL + "="
	}
	
	
}