package life.game.generator

import java.awt.Point
import java.util.ArrayList
import java.util.HashMap
import life.game.gameOfLifeDSL.Condition
import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.GameSpec
import life.game.gameOfLifeDSL.Operator
import life.game.gameOfLifeDSL.Rule

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
	
	def static ArrayList<Point> getCoordinates(GameSpec gameSpec) {
	    val coordinatesList = new ArrayList<Point>()
	    
	    if (gameSpec.coordinates !== null) {
	        for (coordinate : gameSpec.coordinates.coordlist) {
	            // Create a Point and add it to the list
	            coordinatesList.add(new Point(coordinate.x, coordinate.y))
	        }
	    }
	    
	    return coordinatesList
	}
	
	def static Point getGridSize(GameSpec gameSpec) {
		val defaultGrid = new Point(20,20);
	    if (gameSpec.grid !== null) {
	    	val gridSize = new Point(gameSpec.grid.gridNum.x, gameSpec.grid.gridNum.y);
	    	
	    	return gridSize;
	    }
	    
	    return defaultGrid;
	}
	
	
	
}