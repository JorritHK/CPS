	package GameOfLife;

	import java.awt.Point;
	import java.util.ArrayList;

	public class RuleOfLife {
		public static boolean computeCellSurvival(boolean alive, Integer surrounding) {
			// Survival conditions
			if (!alive) {
				// Check if cell should be born
				if ( surrounding == 3 ) {
					return true;
				}
			}
			else {
				// Check if cell should survive
				if ( surrounding == 2 || surrounding == 3 ) {
					return true;
				}
				// Check if cell is killed
				if ( surrounding < 2 ) {
					return false;
				}
			}
			return false;
		}
	}
