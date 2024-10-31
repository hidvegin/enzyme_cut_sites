#!/usr/bin/env python3

import re
import sys
import gzip

def read_fasta(filename):
    """Reads a FASTA sequence from a file, supporting compressed files."""
    sequence = ''
    # Check if the file is gzip-compressed
    if filename.endswith('.gz'):
        open_func = gzip.open
        mode = 'rt'  # Text mode for reading gzip files
    else:
        open_func = open
        mode = 'r'
    with open_func(filename, mode) as f:
        for line in f:
            if not line.startswith('>'):
                sequence += line.strip().upper()
    return sequence

def find_sites(sequence, recognition_seq, cut_pos):
    """Finds the cut sites of enzymes in the sequence."""
    positions = []
    for match in re.finditer('(?={})'.format(recognition_seq), sequence):
        start = match.start()
        cut_site = start + cut_pos
        positions.append(cut_site)  # 0-based position
    return positions

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.fasta")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequence = read_fasta(fasta_file)

    # Define enzymes
    enzymes = {
        'MspI': {'recognition_seq': 'CCGG', 'cut_pos': 1},
        'SphI': {'recognition_seq': 'GCATGC', 'cut_pos': 5}
    }

    # Find cut sites
    enzyme_cuts = {}
    for enzyme, info in enzymes.items():
        positions = find_sites(sequence, info['recognition_seq'], info['cut_pos'])
        enzyme_cuts[enzyme] = positions

    # Calculate total cuts
    total_cuts = {enzyme: len(positions) for enzyme, positions in enzyme_cuts.items()}

    # Combine and sort cut sites
    cuts = []
    for enzyme, positions in enzyme_cuts.items():
        for pos in positions:
            cuts.append((pos, enzyme))
    cuts.sort(key=lambda x: x[0])

    # Count fragments where 5' end is cut by MspI and 3' end by SphI
    count_fragments = 0
    for i in range(len(cuts) - 1):
        if cuts[i][1] == 'MspI' and cuts[i+1][1] == 'SphI':
            count_fragments += 1

    # Write results to output file
    with open('output.txt', 'w') as out_file:
        for enzyme in enzymes.keys():
            out_file.write('{} enzyme cuts at {} sites.\n'.format(enzyme, total_cuts[enzyme]))
        out_file.write('There are {} fragments cut at the 5\' end by MspI and at the 3\' end by SphI.\n'.format(count_fragments))

if __name__ == '__main__':
    main()
