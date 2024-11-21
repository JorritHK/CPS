package life.game.generator

import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.DefaultConsequence
import life.game.gameOfLifeDSL.GameSpec

//import life.game.gameOfLifeDSL.Condition

class JavaGenerator {
	def static toText(GameSpec root)'''
		package GameOfLife;
	
		import java.awt.Point;
		import java.util.ArrayList;
	
		public class RulesOfLife {
			public static boolean computeCellSurvival(boolean alive, Integer surrounding) {
				«getSurvivalCode(root)»
				
			}
			
			public static ArrayList<Point> getPresetCoordinates() {
				«getStartingCoordinates(root)»
			}
			
			public static Point getGridSize() {
				«getGridSize(root)»
			}
		}'''
		
	def static getStartingCoordinates(GameSpec root)'''
		// Add preset points to list
		ArrayList<Point> coords = new ArrayList<>();
		«FOR coord : Util.getCoordinates(root)
			BEFORE "coords.add(new Point("
			SEPARATOR "));\ncoords.add(new Point(" 
			AFTER "));"»«coord.x»,«coord.y» «ENDFOR»
		return coords;
		'''
	
	def static getGridSize(GameSpec root)'''
		// get size of grid
		Point gridSize = new Point(«Util.getGridSize(root).x»,«Util.getGridSize(root).y»);
		
		return gridSize;
		'''
		
		

	def static getSurvivalCode(GameSpec root)'''
		// Survival conditions
		if (!alive) {
			// Check if cell should be born
			«IF !Util.getRuleMap(root).get(Consequence.BORN).isEmpty()
			»«
		'''
			if «FOR cond : Util.getRuleMap(root).get(Consequence.BORN)
				BEFORE "( "
				SEPARATOR " || "
				AFTER " )"»surrounding «Util.getOperatorStr(cond.operator)» «cond.neighbors»«ENDFOR» {
				return true;
			}
		'''»«ENDIF»
		}
		else {
			// Check if cell will survive
			«IF !Util.getRuleMap(root).get(Consequence.SURVIVAL).isEmpty()
			»«'''
			if «FOR cond : Util.getRuleMap(root).get(Consequence.SURVIVAL)
				BEFORE "( "
				SEPARATOR " || "
				AFTER " )"»surrounding «Util.getOperatorStr(cond.operator)» «cond.neighbors»«ENDFOR» {
				return true;
			}'''»«ENDIF»

			// Check if cell is killed 
			«IF !Util.getRuleMap(root).get(Consequence.DEATH).isEmpty()
			»«'''
			if «FOR cond : Util.getRuleMap(root).get(Consequence.DEATH)
				BEFORE "( "
				SEPARATOR " || "
				AFTER " )"»surrounding «Util.getOperatorStr(cond.operator)» «cond.neighbors»«ENDFOR» {
				return false;
			}'''»«ENDIF»
		}
		return «IF (root.rules.^defaultConsequence !== null)
			»«root.rules.^defaultConsequence === DefaultConsequence.SURVIVAL ? 'true' : 'false'
			»«ELSE»false«ENDIF»;
	'''
}