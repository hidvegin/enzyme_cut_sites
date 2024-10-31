Usage Instructions:

	1.	Save the script to a file, for example, enzyme_cut_sites.py.
	2.	Ensure that Python is installed on your system (Python 3 is recommended).
	3.	Run the script from the terminal using the following command, where genome.fa.gz or genome.fasta is the name of your (compressed or uncompressed) FASTA format input file:

 python enzyme_cut_sites.py genome.fa.gz

 or

 python enzyme_cut_sites.py genome.fasta

 4.	The script will create an output.txt file, which contains:
	•	The total number of cuts made by the MspI and SphI enzymes.
	•	The number of fragments where the 5’ end is cut by MspI and the 3’ end is cut by SphI.

Explanation of the Script:

	•	Reading the FASTA File:
	•	The read_fasta function reads the input FASTA file.
	•	It supports both compressed (*.fa.gz) and uncompressed (*.fasta or *.fa) files.
	•	It ignores header lines starting with > and concatenates the sequence lines.
	•	Finding Cut Sites:
	•	The find_sites function uses regular expressions to locate the recognition sequences of the enzymes.
	•	It calculates the cut positions based on the enzyme’s cut position within its recognition sequence.
	•	Processing Enzyme Cuts:
	•	The script defines the enzymes and their properties in the enzymes dictionary.
	•	It finds the cut sites for each enzyme and stores them in enzyme_cuts.
	•	It calculates the total number of cuts for each enzyme.
	•	Counting Specific Fragments:
	•	It combines and sorts all cut sites from both enzymes.
	•	It iterates over the sorted cuts to count fragments where an MspI cut is immediately followed by an SphI cut.
	•	This represents fragments with an MspI cut at the 5’ end and an SphI cut at the 3’ end.
	•	Writing Output:
	•	The script writes the total cuts and the specific fragment count to output.txt.

 MspI enzyme cuts at 3 sites.
SphI enzyme cuts at 2 sites.
There are 2 fragments cut at the 5' end by MspI and at the 3' end by SphI.

Additional Notes:

	•	Zero-Based Positioning:
	•	Positions are zero-based internally for calculations.
	•	This does not affect the final counts but is important for accurate indexing.
	•	Sequence Assumption:
	•	The script assumes that the input FASTA file contains a single continuous sequence.
	•	For multi-sequence FASTA files, additional handling would be required.
	•	Modifying Enzymes:
	•	You can modify or add enzymes in the enzymes dictionary by specifying their recognition sequences and cut positions.
