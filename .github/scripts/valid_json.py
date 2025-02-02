import json
import argparse
import sys

def check_json_validity(file_path):
    errors = []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        print(f"Found {len(data)} airport entries")

        for key, value in data.items():
            if "lat" in value:
                if not isinstance(value["lat"], (float, int)):
                    errors.append(f'Invalid type for "lat" in entry "{key}". Expected float or int, got {type(value["lat"]).__name__}.')
                elif not -90 <= value["lat"] <= 90:
                    errors.append(f'Invalid value for "lat" in entry "{key}". Expected between -90 and 90, got {value["lat"]}.')

            if "lon" in value:
                if not isinstance(value["lon"], (float, int)):
                    errors.append(f'Invalid type for "lon" in entry "{key}". Expected float or int, got {type(value["lon"]).__name__}.')
                elif not -180 <= value["lon"] <= 180:
                    errors.append(f'Invalid value for "lon" in entry "{key}". Expected between -180 and 180, got {value["lon"]}.')

            if "elevation" in value:
                if not isinstance(value["elevation"], int):
                    errors.append(f'Invalid type for "elevation" in entry "{key}". Expected int, got {type(value["elevation"]).__name__}.')

        return errors

    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e}")
    except Exception as e:
        errors.append(f"An unexpected error occurred: {e}")
    
    return errors

def main():
    parser = argparse.ArgumentParser(description="Check if a JSON file is valid and meets specific criteria.")
    parser.add_argument("file", help="The path to the JSON file to validate.")
    args = parser.parse_args()

    errors = check_json_validity(args.file)
    
    if errors:
        print("Validation errors found:")
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("The JSON file is valid.")

if __name__ == "__main__":
    main()
