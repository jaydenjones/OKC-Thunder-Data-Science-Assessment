import csv, sys, math

file_name = sys.argv[1] 

# eFG = (FGM + (0.5*3PM)) / FGA

if __name__ == "__main__":
    

    # Variables
    team_a_fgm = 0
    team_a_3gm = 0
    team_a_fga = 0
    team_a_2pta = 0
    team_a_nc3a = 0
    team_a_c3a = 0
    team_a_2ptm = 0
    team_a_nc3m = 0
    team_a_c3m = 0


    team_b_fgm = 0
    team_b_3gm = 0
    team_b_fga = 0
    team_b_2pta = 0
    team_b_nc3a = 0
    team_b_c3a = 0
    team_b_2ptm = 0
    team_b_nc3m = 0
    team_b_c3m = 0

    
    
    # NOT PARTICULARLY DRY CODE 
    with open(file_name, 'r') as csv_file: # Open data file
        next(csv_file) # skip first row
        csv_reader = csv.reader(csv_file, delimiter=',') 
        for line in csv_reader: # Read line in data file
            hypotenuse = math.hypot(float(line[1]),float(line[2]))
            # line[0] = team, line[1] = x, line[2] = y, line[3] = fgmade

            if line[0] == "Team A":

                if hypotenuse > 22 and float(line[2]) <= 7.8:
                    # print(f"{line[0]}: CORNER 3")
                    if line[3] == '1':
                        team_a_3gm += 1
                        team_a_c3m += 1

                    team_a_fga += 1
                    team_a_c3a += 1
                    

                elif hypotenuse >= 22 and float(line[2]) > 7.8: 
                    # print(f"{line[0]}: NON CORNER 3")
                    if line[3] == '1':
                        team_a_3gm += 1
                        team_a_nc3m += 1
                    team_a_fga += 1
                    team_a_nc3a += 1

                elif hypotenuse < 22 and hypotenuse < 23.75: 
                    # print(f"{line[0]}: TWO POINTER")
                    if line[3] == '1':
                        team_a_fgm += 1
                        team_a_2ptm += 1
                    team_a_fga += 1
                    team_a_2pta += 1
                else:
                    print(line[1],line[2], hypotenuse)


            if line[0] == "Team B":

                if hypotenuse > 22 and float(line[2]) <= 7.8:
                    # print(f"{line[0]}: CORNER 3")
                    if line[3] == '1':
                        team_b_3gm += 1
                        team_b_c3m += 1
                    team_b_fga += 1
                    team_b_c3a += 1
                    


                elif hypotenuse >= 22 and float(line[2]) > 7.8: 
                    # print(f"{line[0]}: NON CORNER 3")
                    if line[3] == '1':
                        team_b_3gm += 1
                        team_b_nc3m += 1
                    team_b_fga += 1
                    team_b_nc3a += 1


                elif hypotenuse < 22 and hypotenuse < 23.75: 
                    # print(f"{line[0]}: TWO POINTER")
                    if line[3] == '1':
                        team_b_fgm += 1
                        team_b_2ptm += 1
                    team_b_fga += 1
                    team_b_2pta += 1
                


    print(f"TEAM A FGA: {team_a_fga}")      
    print(f"TEAM B FGA: {team_b_fga}")      
    print(f"TEAM A SHOT DIST 2PT: {team_a_2pta / team_a_fga}")      
    print(f"TEAM A SHOT DIST NC3: {team_a_nc3a / team_a_fga}")      
    print(f"TEAM A SHOT DIST C3: {team_a_c3a / team_a_fga}")      
    print('')
    print(f"TEAM B SHOT DIST 2PT: {team_b_2pta / team_b_fga}")      
    print(f"TEAM B SHOT DIST NC3: {team_b_nc3a / team_b_fga}")      
    print(f"TEAM B SHOT DIST C3: {team_b_c3a / team_b_fga}") 

    print('')


    # Based on my interpretation of eFG for each a single shot type
    print(f"TEAM A EFG 2PT: {(team_a_2ptm + (0.5*team_a_3gm)) / team_a_fga}") 
    print(f"TEAM A EFG NC3: {(team_a_nc3m + (0.5*team_a_3gm)) / team_a_fga}") 
    print(f"TEAM A EFG C3: {(team_a_c3m + (0.5*team_a_3gm)) / team_a_fga}") 
    print('')

    print(f"TEAM B EFG 2PT: {(team_b_2ptm + (0.5*team_b_3gm)) / team_b_fga}") 
    print(f"TEAM B EFG NC3: {(team_b_nc3m + (0.5*team_b_3gm)) / team_b_fga}") 
    print(f"TEAM B EFG C3: {(team_b_c3m + (0.5*team_b_3gm)) / team_b_fga}") 

