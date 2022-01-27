import os
def output_individual_roll():
    roll_dict = {}
    heading = ["rollno","register_sem","subno","sub_type"]
    data= open("regtable_old.csv", "r")
    data_list =[]
    for row in data:
        data_list.append(row.strip().split(","))
    for row in data_list[1:]:
        rollno, register_sem, _, subno, _, _, _, _, sub_type = row
        if rollno not in roll_dict:
            roll_dict[rollno] = [heading]
            roll_dict[rollno].append([rollno,register_sem,subno,sub_type])
        else:
            roll_dict[rollno].append([rollno,register_sem,subno,sub_type])

    if not os.path.exists("output_individual_roll"):
        os.mkdir("output_individual_roll")

    for rollno in roll_dict:
        location = os.path.join("output_individual_roll", rollno + ".csv")
        with open(location, "w") as f:
            f.write("\n".join((",".join(row)) for row in roll_dict[rollno]))
    return



def output_by_subject():
    subject_dict = {}
    heading = ["rollno","register_sem","subno","sub_type"]
    data= open("regtable_old.csv", "r")
    data_list =[]
    for row in data:
        data_list.append(row.strip().split(","))
    for row in data_list[1:]:
        rollno, register_sem, _, subno, _, _, _, _, sub_type = row
        if subno not in subject_dict:
            subject_dict[subno] = [heading]
            subject_dict[subno].append([rollno,register_sem,subno,sub_type])
        else:
            subject_dict[subno].append([rollno,register_sem,subno,sub_type])

    if not os.path.exists("output_by_subject"):
        os.mkdir("output_by_subject")

    for subno in subject_dict:
        location = os.path.join("output_by_subject", subno + ".csv")
        with open(location, "w") as f:
            f.write("\n".join((",".join(row)) for row in subject_dict[subno]))
    return


output_individual_roll()
output_by_subject()