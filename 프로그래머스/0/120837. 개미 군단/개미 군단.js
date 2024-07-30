function solution(hp) {
    let generalAnt = Math.floor(hp/5)
    let soldierAnt = Math.floor((hp-(5*generalAnt))/3)
    let workAnt =((hp-(5*generalAnt)-(3*soldierAnt))/1)
    return generalAnt+soldierAnt+workAnt}
