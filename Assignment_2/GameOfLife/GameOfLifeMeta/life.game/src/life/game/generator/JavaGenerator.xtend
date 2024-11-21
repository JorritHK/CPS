package life.game.generator

//import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.GameSpec
//import life.game.gameOfLifeDSL.Condition
import life.game.generator.Util

class JavaGenerator {
	def static toText(GameSpec root)'''
		package GameOfLife;
	
		import java.awt.Point;
		import java.util.ArrayList;
	
		public class RulesOfLife {
			public static void computeCellSurvival(boolean alive, Integer surrounding) {
«««				«getSurvivalCode(root)»
				
			}
			
			public static ArrayList<Point> getPresetCoordinates() {
				«getStartingCoordinates(root)»
			}
			
			public static Point getGridSize() {
				«getGridSize(root)»
			}
		}
	'''
	
	def static getStartingCoordinates(GameSpec root)'''
		// Add preset points to list James
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

	

}