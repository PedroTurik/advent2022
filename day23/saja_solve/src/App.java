import java.io.File;
import java.util.HashMap;
import java.util.Scanner;

public class App {
    public static HashMap<Direction, Boolean> check_all(int rowI, int colI, HashMap<Integer, HashMap<Integer, Boolean>> coord) {
        HashMap<Direction, Boolean> ret_map = new HashMap<Direction, Boolean>();

        // check North
        if (coord.containsKey(rowI - 1)){
            for (int i = colI-1; i <= colI+1; i++) {
                if (coord.get(rowI-1).get(i)){
                    ret_map.put(Direction.North, true);
                    break;
                }
            }
            
        }
        // check South
        if (coord.containsKey(rowI + 1)){
            for (int i = colI-1; i <= colI+1; i++) {
                if (coord.get(rowI+1).get(i)){
                    ret_map.put(Direction.South, true);
                    break;
                }
            }
            
        }
        // check West
        for (int i = rowI-1; i <= rowI+1; i++) {
            if (coord.containsKey(i)){
                if (coord.get(i).get(colI - 1)){
                    ret_map.put(Direction.West, true);
                    break;
                }
            }
        }
        // check East
        for (int i = rowI-1; i <= rowI+1; i++) {
            if (coord.containsKey(i)){
                if (coord.get(i).get(colI + 1)){
                    ret_map.put(Direction.East, true);
                    break;
                }
            }
        }
        
        return ret_map;
    }

    public static void rotate(Direction[] order){
        Direction first = order[0];
        for (int i = 0; i < order.length - 1; i++) {
            order[i] = order[i+1];
        }
        order[3] = first;
    }


    public enum Direction{
        North, South, West, East
    }

    /**
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        HashMap<Integer, HashMap<Integer, Boolean>> coord = new HashMap<Integer, HashMap<Integer, Boolean>>();

        File f = new File("input.txt");

        Scanner input = new Scanner(f);
        
        int row = 0;
        while (input.hasNextLine()){
            int col = 0;
            for (int c: input.nextLine().strip().chars().toArray()){
                if (c == 35){
                    if (!coord.containsKey(row)){
                        coord.put(row, new HashMap<Integer, Boolean>());
                    }

                    coord.get(row).put(col, true);
                }
                col++;
            }
            row++;
        }
 
        Direction[] order = {Direction.North, Direction.South, Direction.West, Direction.East};

        
        coord.forEach((rowIndex, rowItems ) -> {
            rowItems.forEach((colIndex, exists) -> {
                HashMap<Direction, Boolean> mapper = check_all(rowIndex, colIndex, coord);
                if (mapper.isEmpty()) {return;}

                for (Direction direction : order) {
                    if (mapper.get(direction)){
                        
                        
                        return;
                    }
                }
            });
        });


    }


}
