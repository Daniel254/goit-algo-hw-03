import argparse
import shutil
from pathlib import Path


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension"
    )
    parser.add_argument(
        "source",
        type=str,
        help="Path to the source directory"
    )
    parser.add_argument(
        "destination",
        type=str,
        nargs="?",
        default="dist",
        help="Path to the destination directory (default: dist)"
    )
    return parser.parse_args()


def copy_file(file_path: Path, dest_dir: Path) -> None:
    """Copy a file to the appropriate subdirectory based on its extension.

    Args:
        file_path: Path to the file to copy
        dest_dir: Base destination directory
    """
    try:
        # Get file extension (without dot)
        extension = file_path.suffix[1:].lower() if file_path.suffix else "no_extension"
        
        # Create subdirectory for this extension
        extension_dir = dest_dir / extension
        extension_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy the file
        dest_file = extension_dir / file_path.name
        shutil.copy2(file_path, dest_file)
        print(f"Copied: {file_path} -> {dest_file}")
        
    except PermissionError:
        print(f"Access error: no permission to copy file {file_path}")
    except OSError as err:
        print(f"Error copying file {file_path}: {err}")


def process_directory(source_dir: Path, dest_dir: Path) -> None:
    """Recursively process a directory and copy files.

    Args:
        source_dir: Path to the source directory
        dest_dir: Path to the destination directory
    """
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                process_directory(item, dest_dir)
            elif item.is_file():
                copy_file(item, dest_dir)
                
    except PermissionError:
        print(f"Access error: no permission to read directory {source_dir}")
    except OSError as err:
        print(f"Error processing directory {source_dir}: {err}")


def main() -> None:
    """Execute the main program logic."""
    args = parse_arguments()

    source_path = Path(args.source)
    dest_path = Path(args.destination)

    if not source_path.exists():
        print(f"Error: source directory '{source_path}' does not exist")
        return

    if not source_path.is_dir():
        print(f"Error: '{source_path}' is not a directory")
        return
    
    # Create destination directory if it doesn't exist
    try:
        dest_path.mkdir(parents=True, exist_ok=True)
        print(f"Destination directory: {dest_path.absolute()}")
    except PermissionError:
        print(f"Error: no permission to create directory '{dest_path}'")
        return
    except OSError as err:
        print(f"Error creating destination directory: {err}")
        return

    print(f"Starting copy from '{source_path}' to '{dest_path}'...")
    process_directory(source_path, dest_path)
    print("Copy completed!")


if __name__ == "__main__":
    main()

