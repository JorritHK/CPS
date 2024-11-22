	package GameOfLife;

	import java.awt.Point;
	import java.util.ArrayList;

	public class RulesOfLife {
		public static boolean computeCellSurvival(boolean alive, Integer surrounding) {
			// Survival conditions
			if (!alive) {
				// Check if cell should be born
				if ( surrounding == 3 || surrounding == 6 ) {
					return true;
				}
			}
			else {
				// Check if cell will survive
				if ( surrounding == 2 || surrounding == 3 ) {
					return true;
				}
			
				// Check if cell is killed 
			}
			return false;
			
		}
		
		public static ArrayList<Point> getPresetCoordinates() {
			// Add preset points to list
			ArrayList<Point> coords = new ArrayList<>();
			coords.add(new Point(50,30));
			coords.add(new Point( 51,29));
			coords.add(new Point( 52,29));
			coords.add(new Point( 53,29));
			coords.add(new Point( 53,30));
			coords.add(new Point( 53,31));
			coords.add(new Point( 52,32));
			coords.add(new Point( 51,33));
			coords.add(new Point( 50,33));
			coords.add(new Point( 49,33));
			coords.add(new Point( 49,32));
			coords.add(new Point( 49,31 ));
			return coords;
		}
		
		public static Point getGridSize() {
			// get size of grid
			Point gridSize = new Point(100,60);
			
			return gridSize;
		}
	}