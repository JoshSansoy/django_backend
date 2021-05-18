def fight(fighterA, fighterB):
    fightLog = []
    
    fightLog.append('\n ------------------- Begin Fight! -------------------')
    while fighterA.health > 0 and fighterB.health > 0:
        attack = fighterA.doAttack()
        fighterB.takeDamage(attack[0])
        fightLog.append(attack[1])

        if fighterB.health > 0:
            attack = fighterB.doAttack()
            fighterA.takeDamage(attack[0])
            fightLog.append(attack[1])

    else:
        print(fightLog)
        if(fighterA.health > 0):
            fightLog.append(fighterA.name + ' wins!')

        if(fighterB.health > 0):
            fightLog.append(fighterB.name + ' wins!')

        return(fightLog)