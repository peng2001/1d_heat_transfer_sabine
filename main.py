import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Process options")
    parser.add_argument('option', choices=['heat_flux', 'temp'], help='Option to run: heat_flux or temp')

    args = parser.parse_args()

    if args.option == 'heat_flux':
        subprocess.run(['python', 'constant_heat_flux_boundaries/run.py'])
    elif args.option == 'temp':
        subprocess.run(['python', 'constant_temp_boundaries/run.py'])

if __name__ == "__main__":
    main()
