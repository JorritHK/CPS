package life.game.generator

import java.awt.Point
import java.util.ArrayList
import life.game.gameOfLifeDSL.GameSpec

class Util {
//	def static HashMap<int, int> getCoordinateMap(GameSpec root) {
//	var ruleMap = new HashMap<Consequence, ArrayList<Condition>>()
//	ruleMap.put(Consequence.DEATH, new ArrayList<Condition>())
//	ruleMap.put(Consequence.LIVE, new ArrayList<Condition>())
//	ruleMap.put(Consequence.BORN, new ArrayList<Condition>())
//	
//	for (Rule r : root.rules.rules) {
//		ruleMap.get(r.consequence).add(r.reason.condition)
//	}
//	return ruleMap;
//	}

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