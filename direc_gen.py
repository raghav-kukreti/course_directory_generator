import os

NAMES = ["FIRST", "SECOND", "THIRD", "FOURTH"]
FOLDER_NAMES = ["Assignments", "Homeworks", "Resources"]
RESOURCE_NAMES = ["ReferenceBooks", "ReferenceLectures", "ReferenceAssignments"]
def main():
	year_num = int(input("Year number (1,2,3..): "))
	sem_num = int(input("Semester number (1,2,3..): "))

	main_dir_name = NAMES[year_num-1] + "YEAR_" + NAMES[sem_num-1] + "SEM"

	os.mkdir(main_dir_name)
	os.chdir(main_dir_name)

	courses = list(input("course codes separated by spaces: ").split(" "))

	for elem in courses:
		os.mkdir(elem)
		os.chdir(elem)
		for new_elem in FOLDER_NAMES:
			os.mkdir(new_elem)

		os.chdir("Resources")
		for resc in RESOURCE_NAMES:
			os.mkdir(resc)

		os.chdir("../..")


if __name__ == '__main__':
	main()