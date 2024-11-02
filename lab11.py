PROTOTIPOS = ('PD', 'PA', 'PTR', 'PTE', 'PC', 'PR', 'PO', 'PV')
PAISAGENS = ('SOA', 'SVM', 'SCO', 'SF1', 'SF2', 'SF3', 'SL', 'SPC')
CONDICOES_CLIMATICAS = ('CC0', 'CC1', 'CC2', 'CN1', 'CN2', 'CN3', 'CN4', 'CV', 'CTA1', 'CTA2', 'CTE1')

TERRENO_PROTO = {
  'PD':  ('TD', 'TA2'),
  'PA':  ('TA1 TA2', 'TD TP TM'),
  'PTR': ('TP TM', 'TAR TO1 TO2'),
  'PTE': ('TP TM', 'TAR TO1 TO2 TC'),
  'PC':  ('TC TM', 'TO1 TO2 TP'),
  'PR':  ('TC TM', 'TO1 TO2'),
  'PO':  ('TO1 TO2', 'TAR TM'),
  'PV':  ('TM', 'TP TC')
}

TERRENO_ADJACENCIA = {
  'TAR': 'TAR TO1 TP TC TM',
  'TO1': 'TAR TO1 TO2 TM',
  'TO2': 'TO1 TO2',
  'TA1': 'TA1 TA2 TP TC TM',
  'TA2': 'TA1 TA2 TD TC TM',
  'TD': 'TA2 TD',
  'TP': 'TAR TA1 TA2 TP TC TM',
  'TC': 'TAR TA1 TA2 TP TC TM',
  'TM': 'TAR TO1 TA1 TA2 TP TC TM'
}

ELEMENTOS = {
  # Scenarios
  'SOA' : ('PA',               'TA1 TA2'),
  'SVM' : ('PTR PTE PR PO',    'TO1 TO2'),
  'SCO' : ('PTR PTE PR PO',    'TO1'),
  'SF1' : ('PTR PTE',          'TP TM'),
  'SF2' : ('PTR PTE',          'TP TM'),
  'SF3' : ('PA PTR PTE',       'TP TM'),
  'SL'  : ('PTR PTE',          'TP TM TC'),
  'SPC' : (PROTOTIPOS,         'TC TM'),
  # Weather conditions
  'CC0' : ('PTR PTE PC PR PO', 'TAR TO1 TO2 TP TC TM'),
  'CC1' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CC2' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CN1' : ('PTE PR PO',        'TAR TP TC TM'),
  'CN2' : ('PTE PC PR PO',     'TAR TP TC TM'),
  'CN3' : ('PTE PC',           'TAR TP TC TM'),
  'CN4' : ('PC',               'TAR TP TC TM'),
  'CV'  : ('PV',               'TP TC TM'),
  'CTA1': ('PD PA',            'TD'),
  'CTA2': ('PD PA PV',         'TD TA2 CV'),
  'CTE1': ('PR',               'TM TO1 TO2'),
  # Animals
  'AMA' : (PROTOTIPOS,         'TD TA2'),
  'AAV' : (PROTOTIPOS,         'TAR TP TA1 TC TM'),
  'AMM' : (PROTOTIPOS,         'TO1 TO2 TAR'),
  'APE' : (PROTOTIPOS,         'TO1 TO2 SL TAR'),
  'AAL' : (PROTOTIPOS,         'TAR TP SL TO1'),
  'ACR' : (PROTOTIPOS,         'TAR TO1'),
  'AHQ' : (PROTOTIPOS,         'TAR TA1 TP TM'),
  'ARO' : (PROTOTIPOS,         'TAR TA1 TA2 TD TC TM'),
  'AFE' : (PROTOTIPOS,         'TAR TA1 TP TC TM SF1'),
  'ACA1': (PROTOTIPOS,         'TP TC TM SF1'),
  'ACA2': (PROTOTIPOS,         'TP TC TM SF1'),
  'AHOT': (PROTOTIPOS,         'TP TC TM SF1 SF2 SF3')
}

def move(matrix, direction, pivot_x, pivot_y):
    dx, dy = 0, 0
    if direction == "N":
        dx, dy = -1, 0
    elif direction == "S":
        dx, dy = 1, 0 
    elif direction == "L":
        dx, dy = 0, 1 
    elif direction == "O":
        dx, dy = 0, -1
    
    new_x, new_y = pivot_x + dx, pivot_y + dy

    max_axis_y = len(matrix[0]) - 1
    max_axis_x = len(matrix) - 1

    # max axis x
    if new_x > max_axis_x:
        return 0, new_y
    if new_y > max_axis_y:
        return new_x, 0

    # max axis y
    if new_x < 0 and new_y < 0:
        return max_axis_x, max_axis_y
    if new_x < 0:
        return max_axis_x, new_y
    if new_y < 0:
        return new_x, max_axis_y
    # if dont exceed
    else:
        return new_x, new_y

def verify_prototype(x, y, item: str, selected_prototype):
    itens = item.split(',')

    for item in itens:
        if item in ELEMENTOS:
            if selected_prototype in ELEMENTOS[item][0]:
                return
            else: 
                return f"{x},{y}:{item}"
        if TERRENO_PROTO.get(selected_prototype):
            if item in TERRENO_PROTO[selected_prototype][0]:
                return 
            if item in TERRENO_PROTO[selected_prototype][1]:
                return
        
        return f"{x},{y}:{item}"

def verify_neighbors(pivot_axis, neighbors, matrix):
    itens = []
    pivot = matrix[pivot_axis[0]][pivot_axis[1]].split(',')[0]
    for neighbor in neighbors:
       itens.append([matrix[neighbor[0]][neighbor[1]], neighbor])
    
    for item in itens:
        terrain = item[0].split(',')[0]
        if TERRENO_ADJACENCIA.get(pivot):
            if not terrain in TERRENO_ADJACENCIA[pivot]:
                return f"{pivot_axis[0]},{pivot_axis[1]}:{pivot}"         


def validate(matrix, selected_prototype):
    rule_one_errors = set()
    rule_two_errors = set()
    rule_three_errors = set()

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            neighbors = []
            for direction in ["O", "L", "N", "S"]:
                x, y = move(matrix, direction, i, j)
                neighbors.append([x, y])

                # rule 1
                is_valid_prototype = verify_prototype(x, y, matrix[x][y], selected_prototype)
                if is_valid_prototype:
                    rule_one_errors.add(is_valid_prototype)
            
            is_valid_neighbor = verify_neighbors([i, j], neighbors, matrix)
            if is_valid_neighbor:
                rule_two_errors.add(is_valid_neighbor)
                

    rule_one_errors = sorted(list(rule_one_errors))
    rule_two_errors = sorted(list(rule_two_errors))
    rule_three_errors = sorted(list(rule_three_errors))

    print('regra 1')
    if rule_one_errors:
        print(*rule_one_errors, sep="\n")
        print('falha')
    else:
        print('ok')

    print('regra 2')
    if rule_two_errors:
        print(*rule_two_errors, sep="\n")
        print('falha')
    else:
        print('ok')

    print('regra 3')
    if rule_three_errors:
        print(*rule_three_errors, sep="\n")
        print('falha')
    else: 
        print('ok')

def main():
    sectors = []

    while True:
        prototype_id = None
        x = None
        y = None

        if not prototype_id and not x and not y:
            prototype_id = input()
            x, y = input().split(' ')
        
        sectors.append(list(filter(None, input.split(' '))))
        
        if len(sectors) == int(x):
          validate(sectors, prototype_id)
          break
            
def test():
    prototype_id = 'PTR'
    x = 4
    y = 4

    # MOCK_SECTORS = [
    #     "TO2     TO2,AMM TO2,AMM     TO1,AAL TO1,AAL TO2,AMM",
    #     "TO2     TO1,AAL TO1,AAL     TO1,AAL TO1,AAL TO2",
    #     "TO2,AMM TO1,AAL TAR,ACR,AAL TM      TAR,ACR TO1,AMM",
    #     "TO2,AMM TO1,AAL TO1,AAL     TO1,AAL TO1,AAL TO2",
    #     "TO2     TO1,AAL TAR,ACR,AAL TO1,AAL TAR,AAL TO1,AMM",
    #     "TO2,AMM TO1,AAL TO1,AAL     TO1,AAL TO1,AAL TO2",
    #     "TO2,AMM TO2,AMM TO2,AMM     TO2     TO2,AMM TO2,AMM"
    # ]
    
    # MOCK_SECTORS_2 = [
    #   "TD,ARO      TD,ARO,CTA2 TD       TA2     TA2,CTA1 TD,CTA1",
    #   "TD,ARO,CTA2 TD,ARO,CTA2 TA2,CTA2 TA2     TA2,CTA1 TD,CTA1",
    #   "TD,ARO      TA2         TA2,CTA2 TM,AMA  TA1      TD",
    #   "TD,ARO,CTA2 TD          TA2,CTA2 TA2     TD       TD",
    #   "TD,CTA2     TA2,ARO     TD       TD,ARO  TD,ARO   TD,AMA",
    #   "TD          TD          TD,ARO   TD,CTA2 TD,ARO   TD,AMA",
    #   "TD,CTA2     TD,ARO      TD,CTA2  TD,ARO  TD,AMA   TD,AMA"
    # ]

    MOCK_SECTORS_3 = [
      "TM,SL,APE   TM        TP,AHQ   TP,AHQ    TP,AHQ",
      "TM TP,SL,AHQ,APE  TP,AHQ    TP,AHQ   TP,AHQ",
      "TM TP,SL,AHQ,APE  TP,SL,AHQ,APE  TM    TAR,ACR",
      "TM TP,AHQ    TAR,AAL    TO1,AMM,APE   TAR,AHQ",
      "TM TP,AHQ    TAR,ACR,AAL   TP,AHQ   TP,AAL"
    ]

    sectors = [list(filter(None, sector.split(' '))) for sector in MOCK_SECTORS_3]
    validate(sectors, prototype_id)

# main()
test()