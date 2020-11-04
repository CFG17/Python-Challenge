import os
import csv

# Data from csv file
Pypoll_path = os.path.join('Resources', 'election_data.csv')

# Create column list
total_votes =[]
voter_ID =[]
county = []
candidate = []
khan =[]
correy=[]
li=[]
otooley=[]

# Enter CSV file

with open(Pypoll_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    #Step to skip header to start counting first row of data
    csv_header = next(csvreader)

    # Count of the total votes

    for row in csvreader:
        voter_ID.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])


    print(voter_ID)
    print(county)
    print(candidate)
    #Count total votes
    total_votes = len(voter_ID)

    #Count vote for each candidate

    for candiate in  candidate:
        if candidate == "Khan":
            khan.append(candidate)
            khan_total_votes = len(khan)
        elif candidate =="Correy":
            correy.append(candidate)
            correy_total_votes = len(correy)
        elif candidate == "Li":
            li.append(candidate)
            li_total_votes = len(li)
        else:
            otooley.append(candidate)
            otooley_total_votes = len(otooley)
    #Calculate percentage of votes for each candidate
    percent_for_khan = (float(khan_total_votes)/(ptotal_votes)*100)
    percent_for_correy = (float(correy_total_votes)/(total_votes)*100)
    percent_for_li = (float(li_total_votes)/(total_votes)*100)
    percent_for_otooley = (float(otooley_total_votes)/(total_votes)*100)

    if        percent_for_khan > max(percent_for_correy,percent_for_li,percent_for_otooley):
              winner_of_election = "Khan"
        
    elif  percent_for_correy > max(percent_for_khan,percent_for_li,percent_for_otooley):
              winner_of_election  = "Correy"

    elif  percent_for_li > max(percent_for_correy, percent_for_khan, percent_for_otooley):
              winner_of_election = "Li"
        
    else:
              winner_of_election = "O'Tooley"

    #Summary of candidates
    candidate_khan = str(percent_for_khan) + "%" + "(" + str(khan_total_votes) + ")"
    candidate_correy = str(percent_for_correy) + "%" + "(" + str(correy_total_votes) + ")"
    candidate_li = str(percent_for_li) + "%" + "(" + str(li_total_votes) + ")"
    candidate_otooley = str(percent_for_otooley) + "%" + "(" + str(otooley_total_votes) + ")"

    #Print election results
    print(" Election Results")
    print("-------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------")
    print("Khan : "  + str(candidate_khan))
    print("Correy : " + str(candidate_correy))
    print("Li : " + str(candidate_li))
    print("O'Tooley: " + str(candidate_otooley))
    print("----------------------")
    print(" The Winner is: " + str(winner_of_election))


       


