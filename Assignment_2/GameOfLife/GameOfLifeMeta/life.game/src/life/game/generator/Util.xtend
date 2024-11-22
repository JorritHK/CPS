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
	    val initialBoard = gameSpec.initial;
	    
	    // Add manual point coordinates
	    if (initialBoard.coordinates !== null) {
	        for (coordinate : initialBoard.coordinates.coordlist) {
	            // Create a Point and add it to the list
	            coordinatesList.add(new Point(coordinate.x, coordinate.y))
	        }
	    }
	    
	    // Add RLE patterns to the initial board Coordinates
	   if (initialBoard.patterns !== null) {
	   	for (p: initialBoard.patterns) {
	   		val x = p.start.x;
	   		val y = p.start.y;
	   		
	   		val char aliveChar = 'o';
	   		
	   		// Get pattern and replace line breaks
	   		val String rle = p.pattern.replace("\n", "").replace("\r", "").replace("\\s", "").replace("!", "");
	   		
	   		val String[] rows = rle.split("\\$");
	   		
	   		for (i: 0 .. rows.size() - 1) {
	   			val curY = y + i;
	   			var curX = x;
	   			
	   			val tokens = rows.get(i).split("(?<=[bo])");
	   			for (t: tokens) { // run count is 1
	   				if (t.length !== 0) {
		   				if (t.length === 1) {
		   					if (t.equals("o")) {
		   						coordinatesList.add(new Point(curX,curY));
		   					}
		   					curX += 1;
		   				}
		   				else { // run_count is not empty
		   					val char tag = t.charAt(t.length() - 1);
		   					val String rest = t.replaceFirst(".$","");
		   					val amount = Integer.valueOf(rest);
		   					if (tag == aliveChar) {
		   						for (j: curX .. curX + amount - 1 ) {
		   							coordinatesList.add(new Point(j, curY));
		   						}
		   					}
		   					curX += amount;
		   				}
	   				}
	   				
   				}
   			}
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