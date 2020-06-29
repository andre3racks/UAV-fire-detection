# UAV Fire Detection

## Getting Started

1. Clone the repository
2. Install python3 (if you haven't already)
3. Install pip3 (if you haven't already)
4. Navigate to the root directory of the project
5. Install the required packages by using `pip3 install -r requirements.txt`

## How to Make Updates to the Project

***Note: NEVER commit straight to master*** 

1. Create a feature branch off of Master (read about git pull requests if you haven't already or contact Nick for help)
2. Make your changes on the branch
3. If you added any packages, add them to the `requirements.txt` file, by using the following command: `pip3 freeze > requirements.txt`
4. Add any new info to the `README` (if necessary)
5. Once done, commit all the changes and make a Pull Request with the following info:
5.1 What the problem you attempted to solve
5.2 How you did it
5.3 Steps to test
6. Fix any merge conflicts (if any) and send a notification to the team
7. Wait for 2+ members of the group to approve
8. Now you can safely merge you branch (***Note: You MUST wait for 2+ approvals***)

## How to Train Data by Drawing Boxes

1. Navigate to the root directory of the project
2. Modify the `drawBoxes.py` file to use whatever data set you want
3. Run `python3 drawBoxes.py`
4. Draw boxes over fire (Must start at top left, going down to bottom right)
5. Once done drawing boxes over all the fires, hit `q` to go to the next file
6. The program will terminate once youre done going though all the images
