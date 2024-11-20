package life.game.generator

import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.GameSpec
//import life.game.gameOfLifeDSL.Condition

class JavaGenerator {
	def static toText(GameSpec root)'''
		package GameOfLife;
	
		import java.awt.Point;
		import java.util.ArrayList;
	
		public class RuleOfLife {
			public static void computeCellSurvival(boolean alive, Integer surrounding) {
				«getSurvivalCode(root)»
			}
		}
	'''
	
	def static getSurvivalCode(GameSpec root)'''
		// Survival conditions
		if «FOR cond : Util.getRuleMap(root).get(Consequence.LIVE)
			BEFORE "( "
			SEPARATOR " || "
			AFTER " )"» "survivors " «cond.operator» «cond.neighbors» «ENDFOR» {
			return True;
		}
		if «FOR cond : Util.getRuleMap(root).get(Consequence.BORN)
			BEFORE "( "
			SEPARATOR " || "
			AFTER " )"»survivors «cond.operator» «cond.neighbors» «ENDFOR» {
			return True;
		}
		if «FOR cond : Util.getRuleMap(root).get(Consequence.DEATH)
			BEFORE "( "
			SEPARATOR " || "
			AFTER " )"» "survivors " «cond.operator» «cond.neighbors» «ENDFOR» {
			return False;
		}
	'''
}