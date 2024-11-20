package life.game.generator

import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.DefaultOption
import life.game.gameOfLifeDSL.GameSpec

//import life.game.gameOfLifeDSL.Condition

class JavaGenerator {
	def static toText(GameSpec root)'''
		package GameOfLife;
	
		import java.awt.Point;
		import java.util.ArrayList;
	
		public class RuleOfLife {
			public static boolean computeCellSurvival(boolean alive, Integer surrounding) {
				«getSurvivalCode(root)»
			}
		}
	'''
	
	def static getSurvivalCode(GameSpec root)'''
		// Survival conditions
		if (!alive) {
			// Check if cell should be born
			if «FOR cond : Util.getRuleMap(root).get(Consequence.BORN)
				BEFORE "( "
				SEPARATOR " || "
				AFTER " )"»surrounding «Util.getOperatorStr(cond.operator)» «cond.neighbors»«ENDFOR» {
				return true;
			}
		}
		else {
			// Check if cell should survive
			if «FOR cond : Util.getRuleMap(root).get(Consequence.SURVIVAL)
				BEFORE "( "
				SEPARATOR " || "
				AFTER " )"»surrounding «Util.getOperatorStr(cond.operator)» «cond.neighbors»«ENDFOR» {
				return true;
			}
			// Check if cell is killed
			if «FOR cond : Util.getRuleMap(root).get(Consequence.DEATH)
				BEFORE "( "
				SEPARATOR " || "
				AFTER " )"»surrounding «Util.getOperatorStr(cond.operator)» «cond.neighbors»«ENDFOR» {
				return false;
			}
		}
		return «IF (root.rules.^default !== null)
			»«root.rules.^default.consequence === DefaultOption.SURVIVAL ? 'true' : 'false'
			»«ELSE»false«ENDIF»;
	'''
}