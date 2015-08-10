import argparse
import sys
import glob
import os
import shutil

def parse_file(in_filepath, out_filepath):
    """
    Parse an input RST file, looking for sections that should be added to
    the file at out_filepath.  If a file at out_filepath exists, it will
    be overwritten.

    Parameters:
        in_filepath (string): A string filepath to an input RST file.
        out_filepath (string): A string filepath to the RST file to which
            parts of the input filepath will be written.

    Returns:
        None.
    """
    in_file = open(in_filepath)
    out_file = None  # don't open the file until we know annotations exists.

    in_primersection = False
    for line in in_file:
        if line.strip() == '.. primer':
            in_primersection = True
            if out_file is None:
                out_file = open(out_filepath, 'w')
        elif line.strip() == '.. primerend':
            in_primersection = False

        if in_primersection:
            out_file.write(line)

    in_file.close()
    if out_file is not None:
        out_file.close()
    else:
        # If we didn't overwrite the file in the first place, remove the file
        # because it shouldn't be there.
        try:
            os.remove(out_filepath)
        except OSError:
            pass


def process_rst(in_dir, out_dir):
    """
    Process the RST files in the source directory, copying them to the dest
    directory.  All folders for annotated files will be copied.

    Parameters:
        in_dir (string): A string filepath to the source directory to analyze.
            This script assumes that all RST files will be located at the top
            level of this directory.
        out_dir (string): A string filepath to the output folder.

    Returns:
        Nothing.
    """
    print 'Analyzing RST for primer'
    print 'Source directory: %s' % in_dir
    print 'Destination directory: %s' % out_dir
    for in_rst_filename in glob.glob(os.path.join(in_dir, '*.rst')):
        out_rst_filename = os.path.join(out_dir,
                                        os.path.basename(in_rst_filename))
        print 'Checking %s for primer annotations' % in_rst_filename
        parse_file(in_rst_filename, out_rst_filename)

        # If the RST file exists, it had annotations.  Copy image files if
        # needed.
        if os.path.exists(out_rst_filename):
            images_base = os.path.basename(os.path.splitext(in_rst_filename)[0])
            img_dirname = "%s_%s" % (images_base, 'images')
            in_images_dir = os.path.join(in_dir, img_dirname)
            out_images_dir = os.path.join(out_dir, img_dirname)

            if os.path.exists(in_images_dir):
                print 'Copying images dir %s' % in_images_dir
                if os.path.exists(out_images_dir):
                    print 'Removing %s' % out_images_dir
                    shutil.rmtree(out_images_dir)
                shutil.copytree(in_images_dir, out_images_dir)


def main_ui(args=None):
    """
    Basic command-line interface for analyzing RST files for parts that should
    be included in the InVEST primer.

    Parameters:
        args=None (list of strings or None): A list of string parameters to
            analyze.  If None, ``sys.argv[1:]`` will be used.

    Returns:
        Nothing.
    """
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description="Extract text for InVEST primer from User's Guide RST source."
    )

    parser.add_argument('-s', required=True, metavar='SOURCEDIR',
                        help='The source directory to analyze')
    parser.add_argument('-d', required=True, metavar='DESTDIR',
                        help='The destination directory')

    args = parser.parse_args(args)
    process_rst(in_dir=os.path.abspath(args.s), out_dir=os.path.abspath(args.d))

if __name__ == '__main__':
    main_ui()
