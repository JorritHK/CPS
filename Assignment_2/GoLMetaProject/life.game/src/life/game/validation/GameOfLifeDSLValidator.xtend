/*
 * generated by Xtext 2.36.0
 */
package life.game.validation

import java.util.ArrayList
import java.util.Arrays
import java.util.stream.IntStream
import life.game.gameOfLifeDSL.Consequence
import life.game.gameOfLifeDSL.Coordinate
import life.game.gameOfLifeDSL.DefaultConsequence
import life.game.gameOfLifeDSL.GameOfLifeDSLPackage
import life.game.gameOfLifeDSL.GameSpec
import life.game.gameOfLifeDSL.PatternRLE
import life.game.gameOfLifeDSL.Rule
import life.game.gameOfLifeDSL.Rules
import org.eclipse.emf.ecore.EObject
import org.eclipse.xtext.validation.Check

/**
 * This class contains custom validation rules. 
 *
 * See https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#validation
 */
class GameOfLifeDSLValidator extends AbstractGameOfLifeDSLValidator {
	

	@Check
	def checkSensibleNeighbors(Rule rule){
		if (rule.reason.condition.neighbors > 8) {
			error('Neighbor condition can not be larger than 8 since a cell has only 8 neighboring cells', rule.reason.condition, GameOfLifeDSLPackage.Literals.CONDITION__NEIGHBORS

			)
		}
	}
	
	@Check
	def defaultNotSet(Rules ruleSet) {
		var DefaultConsequence defaultConsequence = ruleSet.defaultConsequence;
		
		if (defaultConsequence === DefaultConsequence.EMPTY) {
			defaultConsequence = DefaultConsequence.DEATH;
			info("No default outcome specified, meaning cells unaffected by rules will: " + defaultConsequence, GameOfLifeDSLPackage.Literals.RULES__DEFAULT_CONSEQUENCE)
		}
	}
	
	@Check
	def defaultCorrespondsRules(Rules ruleSet) {
		
		var DefaultConsequence defaultConsequence = ruleSet.defaultConsequence;
		
		if (defaultConsequence === DefaultConsequence.EMPTY) {
			defaultConsequence = DefaultConsequence.DEATH;
		}

		for (r: ruleSet.rules) {
			val String dc = defaultConsequence.literal;
			val String rc = r.consequence.literal;
			if (dc.equals(rc)) {
				warning("Rule has same consequence as the default, meaning it will have no effect.", r, GameOfLifeDSLPackage.Literals.RULE__CONSEQUENCE);
			}
		}
		
	}
	
	@Check
	def checkRulesForOverlap(Rules ruleSet) {
		val ArrayList<Integer> affectedInts = new ArrayList();
		
		for (r: ruleSet.rules) {
			if (r.consequence !== Consequence.BORN) {

				val condition = r.reason.condition;
				if (condition.operator.EQUAL !== null) {
			 		if (affectedInts.contains(condition.neighbors)) {
			 			error(
			 			"Rule affects neighbor amount, which is already covered by another rule: " + condition.neighbors,
			 			condition,
			 			GameOfLifeDSLPackage.Literals.CONDITION__NEIGHBORS)
		 			}
		 			affectedInts.add(condition.neighbors);
	 			}
		 		else if (condition.operator.SMALLER !== null) {
		 			val neighborList = IntStream.range(0, condition.neighbors).toArray();
		 			val overlap = getSubsection(affectedInts, new ArrayList(neighborList));
		 			if (overlap.size() > 0) {
		 				error("Rule creates overlap with another previously specified rule" + Arrays.toString(overlap.toArray()),
		 					condition,
		 					GameOfLifeDSLPackage.Literals.CONDITION__NEIGHBORS
		 				)
		 			}
		 			affectedInts.addAll(neighborList);
			 	}
			 	else if (condition.operator.LARGER !== null) {
		 			val neighborList = IntStream.rangeClosed(condition.neighbors + 1, 8).toArray();
		 			val overlap = getSubsection(affectedInts, new ArrayList(neighborList));
		 			if (overlap.size() > 0) {
		 				error("Rule creates overlap with another previously specified rule" + Arrays.toString(overlap.toArray()),
		 					condition,
		 					GameOfLifeDSLPackage.Literals.CONDITION__NEIGHBORS
		 				)
		 			}
		 			affectedInts.addAll(neighborList);
			 	}
		 	}
		}
	}
	
	// helper function to get overlap between neighbor rules
	def static ArrayList<Integer> getSubsection(ArrayList<Integer> A, ArrayList<Integer> B) {
		
		val ArrayList<Integer> result = new ArrayList();
        for (b: B) {
 
            // Removing the elements from the collection
            if (A.contains(b) == true) {
                result.add(b);
            }
        }
        return result;
    }
	
	
	
	
	
	public static val INVALID_COORD = 'invalidCoordinate'
	
	
	// Check whether gridSize exists and give warning if not
	@Check
	def checkGridFalse(GameSpec root) {
		val initial = root.initial;
		if (initial.coordinates !== null && root.grid === null) { // If not grid specified, add warning and different error messages
	    	warning("When no grid is specified, the default size is [100x60]. Example implementation: GridSize = [50 x 70]", null, null);
	    }
	}
	
	
	
	// Check coordinates against grid (or default grid)
	@Check
	def checkCoordinates(Coordinate coordinate) {
		val grid = getRoot(coordinate).grid;
		var int maxX;
		var int maxY;

		if (grid !== null) {
			maxX = grid.gridNum.x;
			maxY = grid.gridNum.y;
			
		} else {
			maxX = 100;
			maxY = 60;
		}
		validateCoordinate(coordinate, maxX, maxY);
	}
	
	
	def GameSpec getRoot(EObject c) {
		var EObject parent = c;
		var EObject root;
		while (parent !== null) {
			root = parent
			parent = root.eContainer();
		}
		return root as GameSpec;
	}
	
	
	
	def validateCoordinate(Coordinate coordinate, int x, int y) {
		// Check coordinates based on user specified grid 
		if (coordinate.x > x) {
        	error("The x-coordinate value: " + coordinate.x +" cannot exceed grid size of " + x + "!",
        		 	coordinate, 
					GameOfLifeDSLPackage.Literals.COORDINATE__X,
					INVALID_COORD            		
        	);
        } if (coordinate.y > y) {
        	error("The y-coordinate value: " + coordinate.y +" cannot exceed grid size of " + y + "!",
        		 	coordinate, 
					GameOfLifeDSLPackage.Literals.COORDINATE__Y,
					INVALID_COORD            		
        	);
        }
	}
	
	@Check
	def validateRLEStructure(PatternRLE rle) {
		
		val String pattern = rle.pattern.replace("\n", "").replace("\r", "").replace("\\s", "");
		
		for (i: 0 .. pattern.length() - 1) {
			val char c = pattern.charAt(i);
			if (!String.valueOf(c).matches("[\\$bo!0-9]")) {
				error(
				"RLE pattern contains unsupported characters: " + c + " at location: " + i,
				GameOfLifeDSLPackage.Literals.PATTERN_RLE__PATTERN
				)
			}
			
		}
	}
	
	//	@Check
//	def checkForCoordinatesSpelling(GameSpec root) {
//	    // Get all issues and check if the word "coordinates" is present in them
//	    val allIssues = validatorContext.getAllIssues()
//	    allIssues.forEach [ issue |
//	        val rawText = issue.data.get(0) // Raw text from the issue
//	        if (rawText != null && rawText.toLowerCase.contains("coordinates")) {
//	            error("Did you mean 'Coordinates'?",
//	                  issue, // Attach the issue to the correct location in the DSL
//	                  GameOfLifeDSLValidator.INVALID_NAME)
//	        }
//	    ]
//	}	
	
}