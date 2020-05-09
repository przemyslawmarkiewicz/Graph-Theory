import functions
import weighted_graph as wg

if __name__ == "__main__":
    A =  [
            [0, 3, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 6, 9, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [9, 4, 6, 0, 0, 0, 1, 2, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 2, 1, 0, 0, 0, 5, 6, 9],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 9, 0, 5, 3, 0]]
    A =  [
            [0, 8, 0, 9, 3, 9, 5],
            [8, 0, 0, 2, 4, 0, 1],
            [0, 0, 0, 0, 0, 4, 0],
            [9, 2, 0, 0, 0, 9, 0],
            [3, 4, 0, 0, 0, 4, 0],
            [9, 0, 4, 9, 4, 0, 0],
            [5, 1, 0, 0, 0, 0, 0]]
    A =  [
            [0, 3, 2, 0, 4, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 6, 9, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [4, 4, 6, 0, 0, 0, 1, 2, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 2, 1, 0, 0, 0, 5, 6, 9],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 9, 0, 1, 3, 0]]

    g = wg.WeightedGraph(A)

    centre = functions.find_centre(g)
    print(centre)

    centre_minimax = functions.find_centre_minimax(g)
    print(centre_minimax)