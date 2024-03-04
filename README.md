# Marvel Universe: Six Degrees of Spider-Man README

## Overview

This program is designed to solve the "Six Degrees of Spider-Man" problem within the Marvel Universe, using data from the "porgat.txt" file available at [this link](https://bioinfo.uib.es/~joemiro/marvel/porgat.txt). The program builds a network graph of Marvel characters and comic book appearances to calculate the minimum number of steps required to link any given Marvel character to Spider-Man, akin to the "Six Degrees of Kevin Bacon" concept in Hollywood.

## Requirements

- Python 3.x
- NetworkX library for Python
- "porgat.txt" file containing the Marvel Universe database, it can be found [here](https://bioinfo.uib.es/~joemiro/marvel/porgat.txt). All credit for this database goes to the creator of the database.

## Features

- **Character Dictionary Creation**: Builds a dictionary mapping character IDs to their names from "porgat.txt".
- **Graph Construction**: Constructs a graph where nodes represent characters and edges represent their appearances in the same comic books.
- **Breadth-First Search Algorithm**: Utilizes a breadth-first search (BFS) algorithm to find the shortest path between Spider-Man and any other character in the graph.
- **Spider-Man Number Calculation**: Calculates the "Spider-Man number" for each character, representing the minimum number of steps required to link them to Spider-Man through shared comic book appearances.

## Setup

1. Install Python 3.x and ensure it is correctly set up on your system.
2. Install NetworkX using pip:

    ```bash
    pip install networkx
    ```

3. Download the "porgat.txt" file from [here](https://bioinfo.uib.es/~joemiro/marvel/porgat.txt) and place it in the same directory as the program.

## Usage

To run the program, execute the script from the command line:

```bash
python marvel_six_degrees.py

```

## How It Works
1. Dictionary Creation: The program first reads "porgat.txt" to create a dictionary of character names keyed by their IDs.
2. Graph Construction: It then reads the file again to construct the network graph, adding nodes for characters and edges for shared comic appearances.
3. Spider-Man Number Calculation: For each character, the program calculates the shortest path to Spider-Man (character ID 5306 in "porgat.txt") using the BFS algorithm, determining the Spider-Man number based on the path length.


## Modifying the Program
You can modify the main() function to calculate the Spider-Man number between different characters by changing the character IDs in the calculateSpidyNum function call.


