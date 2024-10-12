# Se uma campanha fizer um pronunciamento negativo em relação a outra e sua adversária se mantiver neutra: 5 pontos para a primeira e 0 pontos para a segunda
# Se ambas fizeram pronunciamentos negativos em relação a outra: 1 ponto para cada
# Se ambas se mantiverem neutras: 3 pontos para cada

max_inputs = None;
pronouncements = [0]
candidate_one_points = 0
candidate_two_points = 0

def sum_points():
    pronouncements.append(candidate_one_points)
    pronouncements.append(candidate_two_points)
    for item in pronouncements:
        print(item)

while True:
    k = int(input())

    if max_inputs == None:
        if k == 1:
            max_inputs = k
        else:    
            max_inputs = k + 1
        continue

    if len(pronouncements) == 1:
        if k == 1:
            candidate_one_points += 0
            candidate_two_points += 5
        if k == 0:
            candidate_one_points += 3
            candidate_two_points += 3
        
        if max_inputs != 1:
            pronouncements.append(k)
            continue
        if max_inputs == 1:
            sum_points()
            break


    if (len(pronouncements)) <= max_inputs:   
        if k == 0 and pronouncements[-1] == 0:
            candidate_one_points += 3
            candidate_two_points += 3

        if k == 1 and pronouncements[-1] == 0:
            candidate_one_points += 0
            candidate_two_points += 5
        
        if k == 0 and pronouncements[-1] == 1:
            candidate_one_points += 5
            candidate_two_points += 0

        if k == 1 and pronouncements[-1] == 1:
            candidate_one_points += 1
            candidate_two_points += 1
        
        pronouncements.append(k)
        
        if len(pronouncements) == max_inputs:
            pronouncements.pop()
            sum_points()
            break;
        else:
            continue