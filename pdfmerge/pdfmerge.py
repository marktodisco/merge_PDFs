import argparse
import os
from glob import glob
import tkinter as tk
from tkinter.filedialog import askopenfilenames
from typing import List, Tuple, Iterable
import sys
import warnings

from pdfmerge.PDFMerger import PDFMerger

warnings.filterwarnings(
    "ignore", r"Superfluous whitespace found in object header.*")
        

def main(args=None):
    """
    Entry point into the `pdfmerge` program.
    """
    arguments = args or sys.argv[1:]
    input_dir, output_name = parse_arguments(arguments)
    if input_dir is not None:
        files = validate_directory(input_dir)
    else:
        files = get_files(os.getcwd())
    
    if files is not None:
        merge(files, output_name)
    else:
       print('\nCANCELLED\n')


def parse_arguments(args: list) -> Tuple[str, str]:
    """
    Extract command line arguments.

    Parameters
    ----------
    args : list
        Program arguments. See Notes section.

    Returns
    -------
    Tuple[str, str]
        Path to the input directory or None if not specified.
        Name of the output file, or None if not specified.
    
    Notes
    -----
    The only valid arguments are as follows.
    
    -o : Name of output file.
    -d : Name of input directory. Selects all PDfS in the specifed directory.
    """
    parser = argparse.ArgumentParser(prog='pdfmerge',
                                     description="Merge pdf files.")
    
    parser.add_argument('-o', help='Ouput file name.', default=None)
    parser.add_argument('-d', help='Input directory.', default=None)
    parsed_args = parser.parse_args()
    output_name = parsed_args.o
    input_dir = parsed_args.d
    
    return input_dir, output_name


def get_files(work_dir: str = './') -> List[str]:
    """Allow user to select files using a GUI.

    Parameters
    ----------
    work_dir : str, optional
        The working directory, by default './'

    Returns
    -------
    List[str]
        List of file names, or None if no files are selected.
    """
    tk.Tk().withdraw()
    files = askopenfilenames(
        initialdir=work_dir,
        title='Chose files to merge',
        filetypes=(('PDF', '*.pdf'), ('PDF files', '*.pdf')))
    if files == '':
        return None
    return list(files)


def validate_directory(dir_path: str) -> List[str]:
    """
    Get all PDF file names in a directory.

    Parameters
    ----------
    dir_path : str
        Path to the directory that will be searched.

    Returns
    -------
    List[str]
        List of paths to each PDF file in `dir_path`.
    """
    wildcard = os.path.join(dir_path, '*.pdf')
    all_pdfs = glob(wildcard)
    return all_pdfs


def merge(files: List[str], output_name=None):
    """
    Combine separate PDF files into a single document.

    Parameters
    ----------
    files : List[str]
        List of file paths to merge.
    output_name : str, optional
        Path (including file name) to where the merged file will be saved.
        Default is None.
    """
    sort_keys = ask_sort(files)
    if sort_keys is not None:
        files = sort(files, sort_keys)

    if files == '':
        print('Program stopped by user.')
        return
    
    if output_name is None:
        save_path = os.path.abspath('merged.pdf')
    else:
        save_path = os.path.abspath(output_name)
    
    merger = PDFMerger(files, save_path)
    merger.read()
    merger.write()


def sort(in_list: List[str], sort_keys: List[int]) -> List[str]:
    """
    Reorder a list based on new indicies.

    Parameters
    ----------
    in_list : List[str]
        List to be reordered.
    sort_keys : List[int]
        List of indicies by which `in_list` will be sorted.

    Returns
    -------
    List[str]
        Sorted list.
    """
    in_list_old = in_list.copy()
    out_list = [in_list_old[i] for i in sort_keys]
    return out_list


def ask_sort(files: List[str]) -> List[int]:
    """
    Obtain user input, via CLI, about the desired file sorting order.

    Parameters
    ----------
    files : List[str]
        List containing paths to files.

    Returns
    -------
    List[int]
        List of indicies of the dresired sort order.
    """
    print()
    print('The following files will be merged in the order shown.\n')
    print("If you wish to re-order the files, enter their ID's separated by spaces.\n")
    print_files(files)
    print()
    
    invalid_sort = True
    
    while invalid_sort:
        
        sort_keys = input('Updated ID Order: ') or None
        invalid_sort, sort_keys = parse_string_keys(sort_keys)
        
        if not invalid_sort and sort_keys is not None:
            if len(sort_keys) != len(files):
                invalid_sort = True
            
        if invalid_sort:
            print('\nInvalid input. Try again.\n')

    return sort_keys

def parse_string_keys(keys: str, sep: str = ' ') -> List[int]:
    """
    Transform an input string into a list of integers.

    Parameters
    ----------
    keys : str
        String containing delimiter separated integers.
    sep : str, optional
        The delimiter separating integers. The default is ' '.

    Returns
    -------
    List[int]
        List of integers split by `sep`, or False if error occurs.
    """
    if keys is None:
        sort_keys = None
        invalid_sort = False
        print('\nUsing original sort order.\n')
        return invalid_sort, sort_keys
    
    try:
        keys = keys.split(sep)
        keys = [int(k) for k in keys]
        keys = [k-1 for k in keys]  # Decrement by 1, because zero-indexing.
        
        if not is_permation(keys, range(len(keys))):
            invalid_sort = True
        else:
            invalid_sort = False
    
    except Exception:
        keys = False
        invalid_sort = True
        
    return invalid_sort, keys


def is_permation(a: Iterable, b: Iterable) -> bool:
    """
    Test whether one iterable in a permation of another.

    Parameters
    ----------
    a, b : Iterable
        Objects to test permutability.

    Returns
    -------
    bool
        True if `a` is a permutation of `b`. False otherwise.
    """
    for ai in a:
        if ai not in b:
            return False
    return True


def print_files(files: List[str]):
    """
    Display file name and assign them an index.

    Parameters
    ----------
    files : List[str]
        List of files to display via CLI.
    """
    msg_template = '[{}] {}'
    parent = os.path.dirname(files[0])
    print(f'Parent Directory: {parent}')
    for i, f in enumerate(files):
        trimmed_file = f.replace(parent, '')
        print(msg_template.format(i+1, trimmed_file))


if __name__ == '__main__':
    main()
    
